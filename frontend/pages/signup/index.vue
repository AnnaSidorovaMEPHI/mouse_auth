<template>
  <div class="signup_body">
    <form action="action_page">
      <div class="container">
        <h1>Sign Up</h1>
        <p>Please fill this form to create an account.</p>
        <hr />

        <label for="first_name"><b>First Name</b></label>
        <input
          type="text"
          placeholder="Alexander"
          v-model="first_name"
          required
        />
        <hr />

        <label for="second_name"><b>Second Name</b></label>
        <input
          type="text"
          placeholder="Petrov"
          v-model="second_name"
          required
        />
        <hr />

        <label for="email"><b>Email</b></label>
        <input
          type="text"
          placeholder="email@email.com"
          v-model="email"
          required
        />
        <hr />

        <!-- <label for="psw"><b>Password</b></label>
        <input
          type="password"
          placeholder="Enter Password"
          name="psw"
          required
        />

        <label for="psw-repeat"><b>Repeat Password</b></label>
        <input
          type="password"
          placeholder="Repeat Password"
          name="psw-repeat"
          required
        /> -->
      </div>

      <div class="container">
        <p>
          By creating an account you agree to our
          <a href="#">Terms & Privacy</a>.
        </p>
        <p>Already have an account? <a href="#">Sign in</a>.</p>
        <button type="submit" class="registerbtn">Register</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  head() {
    return {
      title: "Sign up",
      meta: [{ hid: "description", name: "description", content: "Test desc" }],
    };
  },
  data: () => ({
    audioChunks: [],
    // password: "",
    phrases: {},
    email: "",
    first_name: "",
    second_name: "",
    count: 0,
    formData: null,
  }),
  methods: {
    signIn() {},
    async getAudioAuth() {
      const formData = this.formData;
      const audioChunks = this.audioChunks;
      const recordAudio = () =>
        new Promise(async (resolve) => {
          const stream = await navigator.mediaDevices.getUserMedia({
            audio: true,
            video: false,
          });
          const mediaRecorder = new MediaRecorder(stream);

          mediaRecorder.addEventListener("dataavailable", (event) => {
            audioChunks.push(event.data);
          });

          const start = () => mediaRecorder.start();

          const stop = () =>
            new Promise((resolve) => {
              mediaRecorder.addEventListener("stop", () => {
                const audioBlob = new Blob(audioChunks, {
                  type: "audio/wav; codecs=opus",
                });
                this.audioChunks = [];
                const voice = new File([audioBlob], `voice${this.count}.wav`, {
                  lastModified: new Date(),
                  type: "audio/wav; codecs=opus",
                });
                formData.append(`audio${this.count}`, voice);
                formData.append(`first_name`, this.first_name);
                formData.append(`second_name`, this.second_name);
                formData.append(`email`, this.email);

                if (this.count === 9) {
                  axios({
                    method: "POST",
                    url: "https://192.168.137.1:5000/signup",
                    data: formData,
                    headers: {
                      "content-type": "multipart/form-data;",
                    },
                  })
                    .then((response) => {
                      if (response.data === "Ok") {
                        alert("Вы успешно зарегистрированы.");
                      } else if (response.data === 1) {
                        alert(
                          "Пользователь с данным email-адресом уже зарегистрирован."
                        );
                      } else {
                        alert("Произошла ошибка.");
                        console.log(response);
                      }
                    })
                    .catch((error) => console.log(error));
                }

                // const audioUrl = URL.createObjectURL(audioBlob);
                // var a = document.createElement("a");
                // a.style.display = "none";
                // a.href = audioUrl;
                // a.download = `voice ${this.count}.wav`;
                // document.body.appendChild(a);
                // a.click();
                // setTimeout(function() {
                //   document.body.removeChild(a);
                //   window.URL.revokeObjectURL(audioUrl);
                // }, 100);

                resolve({ audioBlob });
              });

              mediaRecorder.stop();
            });

          resolve({ start, stop });
        });

      const sleep = (time) =>
        new Promise((resolve) => setTimeout(resolve, time));
      const actionButton = document.getElementById("action");
      this.count += 1;

      if (this.count >= 10) {
        alert("Спасибо, больше нет необходимости записывать звук");
      } else {
        actionButton.disabled = true;
        const recorder = await recordAudio();
        recorder.start();
        await sleep(8000);
        const audio = await recorder.stop();
        alert(`Спасибо, запись звука ${this.count} завершена`);
        actionButton.disabled = false;
      }
    },
  },
  mounted() {
    const formData = new FormData();
    this.formData = formData;
  },
};
</script>

<style>
.signin_block {
  padding-top: 10px;
}
.signup_body {
  position: relative;
  display: flex;
  padding-left: 120px;
}
/* .container {
  width: 500px;
  padding: 20px;
  display: inline-block;
  align-items: justify;
} */
.signup_generated {
  padding-top: 23px;
  padding-left: 50px;
}

/* Full-width input fields */
input[type="text"] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}
div[type="text"] {
  padding-top: 5px;
}

input[type="text"]:focus,
input[type="password"]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit/register button */
.registerbtn {
  background-color: rgb(76, 126, 126);
  color: black;
  font-size: 15px;
  font-weight: bold;
  padding: 16px 20px;
  width: 100%;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  opacity: 0.9;
}

.registerbtn:hover {
  opacity: 1;
}

/* Add a blue text color to links */
a {
  color: rgb(76, 126, 126);
}

/* Set a grey background color and center the text of the "sign in" section */
.signup {
  background-color: #f1f1f1;
  text-align: center;
}
</style>
