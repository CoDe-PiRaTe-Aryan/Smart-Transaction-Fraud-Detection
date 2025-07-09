document.getElementById("predict-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const inputs = document.querySelectorAll(".input-field");
  const values = Array.from(inputs).map(input =>
    input.tagName === "SELECT" ? parseInt(input.value) : parseFloat(input.value)
  );

  if (values.some(val => isNaN(val))) {
    document.getElementById("result").innerText = "❗ Please fill all fields properly.";
    document.getElementById("result").style.color = "orange";
    return;
  }

  const response = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ features: values }),
  });

  const data = await response.json();
  const resultDiv = document.getElementById("result");
  const explanationDiv = document.getElementById("explanation");

  if (data.result === "fraud") {
    resultDiv.innerText = "⚠️ Fraudulent Transaction Detected!";
    resultDiv.style.color = "red";
  } else if (data.result === "safe") {
    resultDiv.innerText = "✅ Transaction is Safe";
    resultDiv.style.color = "green";
  } else {
    resultDiv.innerText = "❌ Error: " + data.error;
    resultDiv.style.color = "black";
  }

  explanationDiv.innerText = data.explanation || "";
});
