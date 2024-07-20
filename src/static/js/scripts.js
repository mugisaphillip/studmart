document.addEventListener("DOMContentLoaded", () => {
    const preview_img = document.querySelector(".product_details .preview-img img")
    if (preview_img != null) {
        document.querySelectorAll(".product_details .img-list img").forEach(img => img.addEventListener("click", () => {
            preview_img.src = img.src;
            img.parentElement.querySelector(".active").classList.remove("active")
            img.classList.add("active")
        }))
    }

    // listen for product remove from cart
    // show confirmation modal
    if (document.querySelectorAll(".trigger-modal-cta") != null) {
        document.querySelectorAll(".trigger-modal-cta").forEach(cta => cta.addEventListener("click", () => {
            const link = cta.getAttribute("data-link")
            // close all open modals
            document.querySelectorAll(".modal.show").forEach(elem => elem.classList.remove("show"))
            // get modal and show on screen
            const modal = document.querySelector(".modal")
            // make link as form action
            modal.querySelector("form").action = link
            modal.classList.add("show")
    
        }))
    }

    // cancel btn in modal should close modal and clear form action
    if (document.querySelector(".modal #cancel_cta") != null) {
        document.querySelector(".modal #cancel_cta").addEventListener("click", () => {
            const modal = document.querySelector(".modal")
            modal.querySelector("form").action = ""
            modal.classList.remove("show")
    
        })
    }

    // profile dropdown 
    if (document.querySelector("#tab-dropdown-cta") != null) {
        document.querySelector("#tab-dropdown-cta").addEventListener("click", () => {
            const dropdown = document.querySelector(".nav-drop")
            const cta_icon = document.querySelector("#tab-dropdown-cta i")
            if (dropdown.classList.contains("show")) {
                dropdown.classList.remove("show")
                cta_icon.classList.remove("fa-close")
                cta_icon.classList.add("fa-user")
            } else {
                dropdown.classList.add("show")
                cta_icon.classList.remove("fa-user")
                cta_icon.classList.add("fa-close")
            }
        })
    }

    // mobile nav
    if (document.querySelector("#mb-nav-activator") != null) {
        document.querySelector("#mb-nav-activator").addEventListener("click", () => {
            const nav = document.querySelector("#mb-nav")
            const cta_icon = document.querySelector("#mb-nav-activator i")
            if (nav.classList.contains("show")) {
                nav.classList.remove("show")
                cta_icon.classList.remove("fa-close")
                cta_icon.classList.add("fa-bars")
            } else {
                nav.classList.add("show")
                cta_icon.classList.remove("fa-bars")
                cta_icon.classList.add("fa-close")
            }
        })
    }
    // mobile search
    if (document.querySelector("#mb-search-activator") != null) {
        document.querySelector("#mb-search-activator").addEventListener("click", () => {
            const nav = document.querySelector("#mb-nav")
            const cta_icon = document.querySelector("#mb-search-activator i")
            if (nav.classList.contains("show")) {
                nav.classList.remove("show")
                nav.classList.remove("search")
                cta_icon.classList.remove("fa-close")
                cta_icon.classList.add("fa-search")
            } else {
                nav.classList.add("show")
                nav.classList.add("search")
                cta_icon.classList.remove("fa-search")
                cta_icon.classList.add("fa-close")
            }
        })
    }
})