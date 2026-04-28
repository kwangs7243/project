document.querySelector("#btn_query")
    .addEventListener("click",async function() {
        const question_type = document.querySelector("#query").value;
        if (question_type === "monthly_summary") {
            const year = document.querySelector("#year").value;
            const month = document.querySelector("#month").value;
            const params = {
                year,
                month
            }
            const result = await requestQuery(question_type,params);
            renderText(result);
        }
        const result = await requestQuery(question_type);
        renderText(result);
    });

document.querySelector("#query")
    .addEventListener("change" , function() {
        const question_type = document.querySelector("#query").value;
        const yearInput = document.querySelector("#year")
        const monthInput = document.querySelector("#month")
        if (question_type === "monthly_summary") {
            yearInput.style.display = "inline-block";
            monthInput.style.display = "inline-block";
        }else {
            yearInput.style.display = "none";
            monthInput.style.display = "none";
        }
    });


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

