document.addEventListener("DOMContentLoaded", function () {

    const ctx = document.getElementById("profitChart");

    if (!ctx) return;

    const revenueData = JSON.parse(ctx.dataset.revenue || "[]");
    const expenseData = JSON.parse(ctx.dataset.expense || "[]");
    const labels = JSON.parse(ctx.dataset.labels || "[]");

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Revenue",
                    data: revenueData,
                    backgroundColor: "#2563eb"
                },
                {
                    label: "Expense",
                    data: expenseData,
                    backgroundColor: "#f59e0b"
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "top"
                }
            }
        }
    });

});
