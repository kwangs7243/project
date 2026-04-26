document.querySelector(".btn.MonthlySummary")
    .addEventListener("click", monthlySummary);

document.querySelector(".btn.CategoryRatio")
    .addEventListener("click", categoryRatio);


async function requestQuery(question_type, params = {}) {
    result = await fetch("/api/query", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            question_type,
            params
        })
    });

    return await result.json();
}
function renderText(result) {
    document.querySelector("#result").textContent = 
    JSON.stringify(result, null, 2);
};

async function monthlySummary() {
    year = document.querySelector("#year").value;
    month = document.querySelector("#month").value;
    result = await requestQuery("monthly_summary", {year,month});
    renderText(result)
};

async function categoryRatio() {
    result = await requestQuery("category_ratio");
    renderText(result);
};