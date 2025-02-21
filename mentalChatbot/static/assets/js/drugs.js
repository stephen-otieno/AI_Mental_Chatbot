document.addEventListener("DOMContentLoaded", function () {
    const faqQuestions = document.querySelectorAll(".faq-question");

    faqQuestions.forEach((question) => {
        question.addEventListener("click", function () {
            const answer = this.nextElementSibling;
            const isVisible = answer.style.display === "block";

            document.querySelectorAll(".faq-answer").forEach((ans) => {
                ans.style.display = "none";
            });

            answer.style.display = isVisible ? "none" : "block";
        });
    });
});

 function toggleChat() {
            let chatbox = document.getElementById("chatbox");
            chatbox.style.display = (chatbox.style.display === "block") ? "none" : "block";
        }

        // Chatbot AI Response
        function handleChat(event) {
            if (event.key === "Enter") {
                let input = document.getElementById("chatInput").value.trim();
                if (input === "") return;

                let chatBody = document.getElementById("chatBody");
                chatBody.innerHTML += <p><i>You:</i> ${input}</p>;
                document.getElementById("chatInput").value = "";

                setTimeout(() => {
                    chatBody.innerHTML += <p><i>AI:</i> Stay strong! Seek support when needed. 😊</p>;
                    chatBody.scrollTop = chatBody.scrollHeight;
                }, 1000);
            }
        }