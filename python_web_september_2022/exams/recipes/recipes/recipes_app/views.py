from django.shortcuts import render, redirect

from recipes.recipes_app.forms import CreateRecipeForm, DeleteRecipeForm
from recipes.recipes_app.models import Recipe
from recipes.recipes_app.validators import ingredients_split


def index(request):
    all_recipes = Recipe.objects.all()

    context = {
        'all_recipes': all_recipes,
    }

    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CreateRecipeForm(instance=recipe)
    else:
        form = CreateRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe)
    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, 'delete.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    recipe_ingredients = ingredients_split(recipe.ingredients)

    context = {
        'recipe': recipe,
        'recipe_ingredients': recipe_ingredients,
    }

    return render(request, 'details.html', context)
