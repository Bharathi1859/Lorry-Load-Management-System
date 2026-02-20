document.addEventListener("DOMContentLoaded", function () {

    const expenseInputs = document.querySelectorAll(".expense");
    const freightInput = document.getElementById("freight");
    const totalExpenseField = document.getElementById("totalExpense");
    const profitField = document.getElementById("profit");

    function calculateTotals() {

        let totalExpense = 0;

        expenseInputs.forEach(input => {
            totalExpense += parseFloat(input.value) || 0;
        });

        let freight = parseFloat(freightInput?.value) || 0;
        let profit = freight - totalExpense;

        if (totalExpenseField) {
            totalExpenseField.innerText = totalExpense.toFixed(2);
        }

        if (profitField) {
            profitField.innerText = profit.toFixed(2);

            if (profit >= 0) {
                profitField.style.color = "#15803d";
            } else {
                profitField.style.color = "#b91c1c";
            }
        }
    }

    expenseInputs.forEach(input => {
        input.addEventListener("input", calculateTotals);
    });

    if (freightInput) {
        freightInput.addEventListener("input", calculateTotals);
    }

});
