document.querySelector("#btn-monthly_summary")
    .addEventListener("click", monthly_summary);

document.querySelector("#btn-category_ratio")
    .addEventListener("click", category_ratio);


async function requestQuery(question_type, params = {}) {
    const res = await fetch("/api/query", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            question_type,
            params
        })
    });

    return await res.json();
}


function renderResult(data) {
    document.getElementById("result").textContent =
        JSON.stringify(data, null, 2);
}


async function monthly_summary() {
    const year = document.getElementById("year").value;
    const month = document.getElementById("month").value;

    const data = await requestQuery("monthly_summary", { year, month });

    renderResult(data);
}


async function category_ratio() {
    const data = await requestQuery("category_ratio");

    renderResult(data);
}