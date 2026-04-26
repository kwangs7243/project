document.querySelector("#btn_query")
    .addEventListener("click",async function() {
        const question_type = document.querySelector("#query").value;
        const result = await requestQuery(question_type);
        renderText(result);
    });

document.querySelector("#category_ratio")
    .addEventListener("click", category_ratio);


async function requestQuery(question_type, params = {}) {
    const result = await fetch("/api/query", {
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

