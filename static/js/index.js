var a = document.querySelector(".navbar-toggler");
var b = document.querySelector(".content");
function MainAppear() {
  b.classList.toggle("content_active");
}

// считываем все элементы
const body = document.body;
const btn = document.querySelector("#btn_new");
const modal = document.querySelector("#modal_new");
const modal_detail = document.querySelector("#modal_change");

// обработчики клика на кнопки
btn.addEventListener("click", btnHandler);

// при нажатии на кнопку Click me
function btnHandler(e) {
  e.preventDefault();
  body.classList.add("lock"); // блокируем скролл веб-страницы
  modal.classList.add("modal--open"); // открываем модальное окно

}

// при нажатии на пустое пространство - закрываем окно
window.addEventListener("click", function (e) {
  if (e.target == modal) {
    body.classList.remove("lock");
    modal.classList.remove("modal--open");
  }
});
window.addEventListener("click", function (e) {
  if (e.target == modal_detail) {
    body.classList.remove("lock");
    modal_detail.classList.remove("modal--open");
    this.history.back();
  }
});

function colorchanger(op) {
  var color = op.options[op.selectedIndex].getAttribute('name');
  op.style.backgroundColor = color;
}