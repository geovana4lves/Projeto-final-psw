document.addEventListener("DOMContentLoaded", function () {

    const forms = document.querySelectorAll(".admin-form");

    forms.forEach(function (form) {

        const fields = form.querySelectorAll(
            "input, select, textarea"
        );

        fields.forEach(function (field) {

            if (field.type === "hidden") {
                return;
            }

            if (
                field.type === "checkbox" ||
                field.type === "radio"
            ) {
                field.classList.add("form-check-input");
                return;
            }

            if (field.tagName === "SELECT") {
                field.classList.add("form-select");
            } else {
                field.classList.add("form-control");
            }

        });

    });

});