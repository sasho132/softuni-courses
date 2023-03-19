function validate() {
    const inputEl = document.getElementById("email");
    inputEl.addEventListener("change", validateEmail);

    function validateEmail(e) {
        let text = e.currentTarget.value;
        let condition = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!text.match(condition)) {
            e.currentTarget.classList.add("error");
            return;
        }

        e.currentTarget.classList.remove("error");
        return;
    }
}

//Email Regex - /^[^\s@]+@[^\s@]+\.[^\s@]+$/
