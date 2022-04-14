document.addEventListener("DOMContentLoaded", () => {
  const $navbarBurgers = Array.prototype.slice.call(
    document.querySelectorAll(".navbar-burger"),
    0
  );

  if ($navbarBurgers.length > 0) {
    $navbarBurgers.forEach((el) => {
      el.addEventListener("click", () => {
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        el.classList.toggle("is-active");
        $target.classList.toggle("is-active");
      });
    });
  }

  $(".button").click(function () {
    var buttonId = $(this).attr("id");
    $("#modal-container").removeAttr("class").addClass(buttonId);
    $("body").addClass("modal-active");
  });

  $("#modal-container").click(function () {
    $(this).addClass("out");
    $("body").removeClass("modal-active");
  });
});
