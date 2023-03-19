var settingsDropdown = document.getElementById("user-menu-dropdown");
var adminButton = document.getElementById("admin-settings");;
var tagsDropdown = document.getElementById("tags-menu-dropdown");
var tagsButton = document.getElementById("tags-button");


function toggleUserMenu() {
    if (settingsDropdown.style.display === "none") {
        settingsDropdown.style.display = "block";
    } else {
        settingsDropdown.style.display = "none";
    }
}

function toggleTagsMenu() {
    if (tagsDropdown.style.display === "none") {
        tagsDropdown.style.display = "block";
    } else {
        tagsDropdown.style.display = "none";
    }
}

window.addEventListener("click", function(event) {
    if (settingsDropdown && !adminButton.contains(event.target) && !settingsDropdown.contains(event.target)) {
        settingsDropdown.style.display = "none";
    }

    if (tagsDropdown && !tagsButton.contains(event.target) && !tagsDropdown.contains(event.target)) {
        tagsDropdown.style.display = "none";
    }
});


