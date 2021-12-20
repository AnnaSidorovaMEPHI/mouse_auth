<template>
  <div class="signin_main">
    <div class="signin">
      <h1>Sign in</h1>
      <div class="signin_email">
        <p>Your email:</p>
        <input type="login" v-model="email" placeholder="email@mail.com" />
      </div>
      <div class="signin_password">
        <p>Your password:</p>
        <input
          type="password"
          required
          autocomplete="off"
          v-model="password"
          placeholder="password"
        />
        <p class="forgot"><a href="#">Forgot Password?</a></p>
      </div>
      <div class="signin_button">
        <button
          id="action"
          class="signin_button--microphone"
          v-on:click="getAudioAuth"
        >
          <img src="~/static/img/microphone.png" />
        </button>
      </div>

      <!-- <div>
        <button class="signin_button--signin" v-on:click="signIn">
          Sign in
        </button>
      </div> -->
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  head() {
    return {
      title: "Sign in",
      meta: [{ hid: "description", name: "description", content: "Sign in" }]
    };
  },
  data: () => ({
    email: "",
    password: "",
    count: 0
  }),
  methods: {
    // signIn() {
    // var body = {
    //   userName: "Fred",
    //   userEmail: "Flintstone@gmail.com"
    // };
    // axios({
    //   method: "post",
    //   url: "https://192.168.0.12:5000",
    //   data: body
    // })
    //   .then(function(response) {
    //     console.log(response);
    //   })
    //   .catch(function(error) {
    //     console.log(error);
    //   });
    // const signData = {
    //   email: this.email,
    //   password: this.password,
    //   voice: this.audioBlob
    // };
    // axios
    //   .post("https://192.168.0.12:5000", signData)
    //   .then(response => console.log(response))
    //   .catch(error => console.log(error));
    // },
    async getAudioAuth() {
       axios
	      .get("https://192.168.137.1:5000/phrase")
	      .then(response => (this.phrase = response.data))
	      .catch(error => console.log(error));
      const recordAudio = () =>
        new Promise(async resolve => {
          const audioChunks = this.audioChunks;
          const stream = await navigator.mediaDevices.getUserMedia({
            audio: true,
            video: false
          });
          const mediaRecorder = new MediaRecorder(stream);

          mediaRecorder.addEventListener("dataavailable", event => {
            audioChunks.push(event.data);
          });

          const start = () => mediaRecorder.start();

          const stop = () =>
            new Promise(resolve => {
              mediaRecorder.addEventListener("stop", () => {
                const audioBlob = new Blob(audioChunks, {
                  type: "audio/wav; codecs=opus"
                });
                const voice = new File([audioBlob], `voice ${this.count}.wav`, {
                  lastModified: new Date(),
                  type: "audio/wav; codecs=opus"
                });
                const formData = new FormData();
                formData.append("audio", voice);
                formData.append("email", this.email);
                // formData.append("password", this.password);

                var xhr = new XMLHttpRequest();
                xhr.open("POST", "https://192.168.137.1:5000/signin", true);
                xhr.send(formData);
                xhr.onload = () => {
                  if (xhr.status != 200) {
                    alert(`Error ${xhr.status}: ${xhr.statusText}`);
                  } else if (xhr.responseText === "True") {
                    alert("Успешная аутентификация");
                    this.$nuxt.$router.replace({ path: "/" });
                  } else {
                    alert("Ошибка авторизации, попробуйте еще раз");
                  }
                };
                xhr.onerror = () => {
                  alert("Ошибка POST запроса");
                };

                // const audioUrl = URL.createObjectURL(audioBlob);
                // var a = document.createElement("a");
                // a.style.display = "none";
                // a.href = audioUrl;
                // a.download = `voice.wav`;
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

      const sleep = time => new Promise(resolve => setTimeout(resolve, time));
      const actionButton = document.getElementById("action");
      this.count += 1;

      if (this.count >= 2) {
        alert("Спасибо, больше нет необходимости записывать звук");
      } else {
        actionButton.disabled = true;
        const recorder = await recordAudio();
        recorder.start();
        await sleep(8000);
        const audio = await recorder.stop();
        alert(`Спасибо, запись звука завершена`);
        actionButton.disabled = false;
      }
    }
  },
  mounted() {
  }
};
</script>

<style>
.signin_main {
  width: 100%;
  position: relative;
}
.signin {
  margin-top: 30px;
  margin-left: auto;
  margin-right: auto;
  /* position: absolute; */
  top: 30%;
  width: 400px;
  height: 600px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  align-items: center;
  border: 1px solid #000000;
  box-shadow: 5px;
}
.signin_button {
  padding-top: 10px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  align-items: center;
}
.signin_button--microphone {
  background: rgb(76, 126, 126);
  border-radius: 50%;
  height: 6em;
  width: 6em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: none;
  text-decoration: none;
}
.signin_button--microphone:hover {
  background-color: rgb(224, 59, 59);
}
.signin_button--microphone:active:after,
.signin_button--microphone:focus:after {
  outline: none !important;
  box-shadow: 5px 5px 20px rgb(81, 224, 210), -5px -5px 20px rgb(81, 224, 210);
  background-color: rgb(224, 59, 59);
}
.signin_button--microphone img {
  /* padding-left: 1.9px; */
  height: 4rem;
  width: 4rem;
}
.signin_button--signin {
  margin-top: 10px;
  font-size: 20px;
}
.signin_generated {
  text-align: left;
  width: 250px;
  padding-left: 20px;
  padding-bottom: 20px;
  /* align-items: center; */
}
.signin_email {
  padding-top: 40px;
  /* text-align: center; */
}
/* .signin_generated--phrase {
  text-align: center; 
  position: relative;
} */
</style>
