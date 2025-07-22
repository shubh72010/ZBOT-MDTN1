document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");

  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!username || !password) {
      alert("Please fill in both fields.");
      return;
    }

    try {
      const response = await fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      const result = await response.json();

      if (response.ok) {
        // Login success — redirect or show message
        alert("Logged in successfully!");
        window.location.href = "/dashboard"; // or wherever your dashboard is
      } else {
        alert(result.error || "Login failed.");
      }
    } catch (error) {
      console.error("Login error:", error);
      alert("Server error occurred.");
    }
  });
});