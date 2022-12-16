addEventListener('DOMContentLoaded', () => {
    const button_nav = document.querySelector('.button-nav')
    if (button_nav) {
        button_nav.addEventListener('click', () => {
            const nav_content = document.querySelector('.nav-content')
            nav_content.classList.toggle('public')
            const button_nav_color = document.querySelector('.button-nav')
            button_nav_color.classList.toggle('change-color')
        })
    }
})