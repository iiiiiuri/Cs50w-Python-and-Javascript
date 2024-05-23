document.addEventListener("DOMContentLoaded", function () {
  // Use buttons to toggle between views
  document
    .querySelector("#inbox")
    .addEventListener("click", () => load_mailbox("inbox"));
  document
    .querySelector("#sent")
    .addEventListener("click", () => load_mailbox("sent"));
  document
    .querySelector("#archived")
    .addEventListener("click", () => load_mailbox("archive"));
  document.querySelector("#compose").addEventListener("click", compose_email);
  document
    .querySelector("#compose-form")
    .addEventListener("submit", send_email);

  load_mailbox("inbox");
});

function compose_email() {
  document.querySelector("#emails-view").style.display = "none";
  document.querySelector("#compose-view").style.display = "block";

  document.querySelector("#compose-recipients").value = "";
  document.querySelector("#compose-subject").value = "";
  document.querySelector("#compose-body").value = "";
}
function load_mailbox(mailbox) {
  document.querySelector("#compose-view").style.display = "none";
  document.querySelector("#emails-view").style.display = "block";
  document.querySelector(
    "#emails-view"
  ).innerHTML = `<h1 class='text-emerald-200 text-2xl'>${
    mailbox.charAt(0).toUpperCase() + mailbox.slice(1)
  }</h1>`;

  fetch(`/emails/${mailbox}`)
    .then((response) => response.json())
    .then((emails) => {
      emails.forEach((email) => {
        const emailDiv = document.createElement("div");
        emailDiv.innerHTML = `
          <div class="border rounded p-2  ${
            email.read ? "bg-gray-300" : "bg-white"
          } flex mb-2">

          <h5 class="text-orange-500 ml-2">
          From:
          <span class="text-emerald-800">
             ${email.sender}
          </span>
          </h5>

          <h5 class="text-orange-500 ml-2">
          Subject:
          <span class="text-emerald-800">
             ${email.subject}
          </span>
          </h5>

          <h5 class="text-orange-500 ml-2">
          Timestamp:
          <span class="text-emerald-800">
             ${email.timestamp}
          </span>
          </h5>
          
          </div>`;
        document.querySelector("#emails-view").append(emailDiv);

        emailDiv.addEventListener("click", () => {
          show_email(email.id, mailbox);
        });
      });
    });
}

function show_email(id, mailbox) {
  fetch(`/emails/${id}`)
    .then((response) => response.json())
    .then((email) => {
      document.querySelector("#emails-view").style.display = "none";
      document.querySelector("#compose-view").style.display = "none";

      const emailView = document.querySelector("#emails-view");
      emailView.style.display = "block";
      emailView.innerHTML = `
      <div class="border rounded mt-10 bg-gray-800 bg-opacity-55">

      <div class="flex justify-between bg-gray-900 p-2 border-white border-b-2">
        <h1 class="text-emerald-200 text-2xl">${email.subject}</h1>
        <h5 class="text-emerald-200 italic">From: ${email.sender}</h5>
      </div>

      <div class="p-2">
          <h5 class="text-orange-500">
          Timestamp: 
            <span class="text-emerald-200">
              ${email.timestamp}
            </span>
          </h5>


          <h5 class="text-orange-500">
          Body: 
            <p class="ml-2 text-emerald-200">${email.body}</p>
          </h5>
      </div>

      </div>
        `;

      const replyButton = document.createElement("button");
      replyButton.textContent = "Reply";
      replyButton.className =
        "rounded-md p-2 bg-emerald-900 hover:bg-emerald-200 text-emerald-200 hover:text-gray-900 transition-all delay-0 font-semibold mt-2";
      emailView.append(replyButton);

      replyButton.addEventListener("click", () => {
        document.querySelector("#compose-view").style.display = "block";
        document.querySelector("#emails-view").style.display = "none";
        document.querySelector("#compose-recipients").value = email.sender;
        document.querySelector("#compose-subject").value =
          email.subject.startsWith("Re: ")
            ? email.subject
            : `Re: ${email.subject}`;
        document.querySelector(
          "#compose-body"
        ).value = `\n\nOn ${email.timestamp} ${email.sender} wrote:\n${email.body}`;
      });

      if (mailbox === "inbox" || mailbox === "archive") {
        const archiveButton = document.createElement("button");
        archiveButton.textContent = email.archived ? "Unarchive" : "Archive";
        archiveButton.className =
          "rounded-md p-2 bg-emerald-900 hover:bg-emerald-200 text-emerald-200 hover:text-gray-900 transition-all delay-0 font-semibold mt-2 ml-2";
        emailView.append(archiveButton);

        archiveButton.addEventListener("click", () => {
          fetch(`/emails/${id}`, {
            method: "PUT",
            body: JSON.stringify({
              archived: !email.archived,
            }),
          }).then(() => {
            document.querySelector("#emails-view").style.display = "block";
            document.querySelector("#emails-view").style.display = "none";
            load_mailbox("inbox");
          });
        });
      }

      if (mailbox === "inbox") {
        fetch(`/emails/${id}`, {
          method: "PUT",
          body: JSON.stringify({
            read: true,
          }),
        });
      }
    });
}

function send_email(event) {
  event.preventDefault();
  const recipients = document.querySelector("#compose-recipients").value;
  const subject = document.querySelector("#compose-subject").value;
  const body = document.querySelector("#compose-body").value;

  fetch("/emails", {
    method: "POST",
    body: JSON.stringify({
      recipients: recipients,
      subject: subject,
      body: body,
    }),
  })
    .then((response) => response.json())
    .then((result) => {
      console.log(result);
      load_mailbox("sent");
    });
}
