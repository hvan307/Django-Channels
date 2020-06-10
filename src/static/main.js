// $(document).ready(function () {
//   $('#action_menu_btn').click(function () {
//     $('.action_menu').toggle()
//   })
// })

function main() {
  const actionMenuBtn = document.querySelector('#action_menu_btn')

  function toggleMenu() {
    actionMenuBtn.classList.toggle('action_menu')
  }

  actionMenuBtn.addEventListener('click', toggleMenu)
}

window.addEventListener('DOMContentLoaded', main)