function lockedProfile() {
    let profileButtons = Array.from(document.querySelectorAll(".profile button"));
    profileButtons.map((bn) => bn.addEventListener("click", showInfo));

    function showInfo(event) {
        let profile = event.target.parentElement;
        let isActive = profile.querySelector("input[value='unlock']").checked;
        let profileInfo = profile.querySelector('div');

        if (isActive) {
            if (event.target.textContent === "Show more") {
                profileInfo.style.display = "block";
                event.target.textContent = "Hide it";
            } else {
                profileInfo.style.display = "none";
                event.target.textContent = "Show more";
            }
        }
        return;
    }
}
