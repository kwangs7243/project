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


function renderTable(rows) {
    if (!rows || rows.length === 0) {
        result.innerHTML = "<p>데이터가 없습니다.</p>";
        return;
    }

    const columns = Object.keys(rows[0]);

    let html = "<table border='1'>";
    html += "<tr>";

    columns.forEach(col => {
        html += `<th>${col}</th>`;
    });

    html += "</tr>";

    rows.forEach(row => {
        html += "<tr>";
        columns.forEach(col => {
            html += `<td>${row[col]}</td>`;
        });
        html += "</tr>";
    });

    html += "</table>";

    result.innerHTML = html;
}

function renderResponse(response) {
    if (!response.ok) {
        result.textContent = response.message;
        return;
    }

    if (Array.isArray(response.data)) {
        renderTable(response.data);
        return;
    }

    result.textContent = JSON.stringify(response.data, null, 2);
}

async function monthly_summary() {
    const year = document.getElementById("year").value;
    const month = document.getElementById("month").value;

    const response = await requestQuery("monthly_summary", { year, month });
    renderResponse(response);
}


async function category_ratio() {
    const response = await requestQuery("category_ratio");
    renderResponse(response);
}