function extract(content) {
    const el = document.getElementById(content);
    let result = [];
    let text = el.textContent;
    let pattern=/\(([^)]+)\)/g;
    let match = pattern.exec(text);
    while (match) {
        result.push(match[1]);
        match=pattern.exec(text);
    }
    
    return result.join('; ');
}