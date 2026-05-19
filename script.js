async function getRecommendation() {
    const budget = document.getElementById("budget").value;
    const priority = document.getElementById("priority").value;

    const res = await fetch("http://127.0.0.1:8000/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            budget: parseInt(budget),
            priority: priority
        })
    });

    const data = await res.json();

    document.getElementById("result").innerText =
        JSON.stringify(data, null, 2);
}