<template>
  <div class="container flex justify-start">
    <div class="my-4 mx-4 overflow-x-auto">
      <div class="align-middle inline-block min-w-full">
        <div class="shadow overflow-hidden sm:rounded-lg">
          <table
            class="min-w-full divide-y divide-purple-300 border-solid border-2 border-purple-200"
          >
            <thead class="bg-purple-200">
              <tr>
                <th
                  v-for="user_header in user_headers"
                  :key="user_header.id"
                  scope="col"
                  class="px-6 py-3 text-center text-xs font-medium text-gray-600 uppercase tracking-wider"
                >
                  {{ user_header }}
                </th>
                <th scope="col" class="relative px-6 py-3">
                  <span class="sr-only">Edit</span>
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-purple-200">
              <tr v-for="user in users" :key="user.id">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 h-10 w-10">
                      <img
                        :src="user.image"
                        alt=""
                        class="w-10 h-10 rounded-full object-cover content-center border-4 border-purple"
                      />
                    </div>
                    <div class="ml-4">
                      <div class="text-sm font-medium text-purple-900">
                        {{ user.name }}
                      </div>
                      <div class="text-sm text-gray-600">
                        {{ user.email }}
                      </div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-purple-900">
                    {{ user.position }}
                  </div>
                  <div class="text-sm text-gray-600">{{ user.sphere }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span
                    class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-purple-100 text-gray-800"
                  >
                    {{ user.status }}
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                  {{ user.role }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
                >
                  <a href="#" class="text-indigo-600 hover:text-indigo-900"
                    >Edit</a
                  >
                </td>
              </tr>
              <!-- More people... -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="w-1/2 my-4 mx-6">
      <div class="w-full sm:rounded-lg border-solid border-2 border-purple-200">
        <div class="bg-white text-center rounded-lg">
          <div class="flex justify-center">
            <img
              src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60"
              alt=""
              class="w-20 h-20 rounded-full object-cover content-center mt-5 border-4 border-purple"
            />
          </div>
          <h1 class="text-center font-bold tracking-wider text-gray-700 mt-4">
            Jane Cooper
          </h1>
          <p class="text-gray-500 mt-1 text-center">
            Moscow, Kolotushkina Street, 10A
          </p>
          <br />
          <button
            class="py-2 px-4 rounded-full text-white text-sm font-semibold inline-flex leading-5 font-semibold bg-purple-100 text-gray-800"
          >
            Verified
          </button>

          <div class="my-5 flex justify-between mx-8">
            <div class="text-left">
              <h1 class="text-gray-500">Orders</h1>
              <p class="text-3xl text-gray-800">78</p>
            </div>
            <div class="text-left">
              <h1 class="text-gray-500">Phone</h1>
              <p class="text-3xl text-gray-800">+79075004030</p>
            </div>
            <div class="text-left">
              <h1 class="text-gray-500">Registered</h1>
              <p class="text-3xl text-gray-800">14.10.2017</p>
            </div>
          </div>
          <div class="my-5 flex justify-between mx-8">
            <div class="text-left">
              <h1 class="text-gray-500">Credit Card</h1>
              <span
                class="px-4 py-1 mt-2 inline-flex leading-5 font-semibold rounded-full bg-green-200 text-gray-800"
              >
                Yes
              </span>
            </div>
            <div class="text-left">
              <h1 class="text-gray-500">Email</h1>
              <p class="text-3xl text-gray-800">jane.cooper@example.com</p>
            </div>
            <div class="text-left">
              <h1 class="text-gray-500">Role</h1>
              <p class="text-3xl text-gray-800">Client</p>
            </div>
          </div>
        </div>
        <div class="bg-white rounded-lg text-center my-10 mx-6">
          <h1 class="text-xl fond-bold tracking-wider text-gray-800">
            Transactions
          </h1>
          <div
            class="mt-2 bg-white border border-purple-light shadow-lg rounded"
          >
            <table class="text-center w-full">
              <thead>
                <tr>
                  <th
                    v-for="transaction_header in transaction_headers"
                    :key="transaction_header.id"
                    class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light"
                  >
                    {{ transaction_header }}
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="transaction in transactions"
                  :key="transaction.id"
                  class="hover:bg-grey-lighter"
                >
                  <td
                    class="text-purple-900 py-2 px-2 border-b border-grey-light cursor-pointer"
                    @click="setGet('transaction')"
                  >
                    <a :href="'transactions/' + transaction.id">{{
                      "#" + transaction.id
                    }}</a>
                  </td>
                  <td class="py-2 px-2 border-b border-grey-light">
                    <div class="text-sm font-medium text-purple-900">
                      {{ transaction.time }}
                    </div>
                    <div class="text-sm text-gray-600">
                      {{ transaction.date }}
                    </div>
                  </td>
                  <td class="py-2 px-2 border-b border-grey-light">
                    {{ transaction.operation }}
                  </td>
                  <td class="py-2 px-2 border-b border-grey-light">
                    {{ transaction.source }}
                  </td>
                  <td class="py-2 px-2 border-b border-grey-light">
                    {{ transaction.total }}
                  </td>
                  <td class="py-2 px-2 border-b border-grey-light">
                    {{ transaction.card }}
                  </td>
                  <td
                    class="text-purple-900 py-2 px-2 border-b border-grey-light"
                  >
                    {{ transaction.order }}
                  </td>
                </tr>
              </tbody>
            </table>
            <div class="w-full text-right">
              <button
                class="bg-transparent hover:bg-purple-400 text-purple-500 font-semibold hover:text-white py-2 px-10 border border-purple-500 hover:border-transparent rounded-full my-4 mx-6"
              >
                See more
              </button>
            </div>
          </div>
          <div class="mt-4 w-full">
            <p class="font-bold tracking-wider text-gray-800">Documents</p>
            <p class="text-gray-500 mt-2">
              Please check the user's documents, if everything is in order, then
              set the status to "Verified".
            </p>
            <div class="bg-white shadow-md rounded my-6">
              <table class="text-left w-full border-collapse" id="documents">
                <!--Border collapse doesn't work on this site yet but it's available in newer tailwind versions -->
                <thead>
                  <tr>
                    <th
                      class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light"
                    >
                      Document
                    </th>
                    <th
                      class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light"
                    >
                      Actions
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="document in documents"
                    :key="document.id"
                    class="hover:bg-grey-300"
                  >
                    <td
                      class="underline py-4 px-6 border-b border-grey-light text-purple-900"
                    >
                      {{ document }}
                    </td>
                    <td
                      class="py-4 px-6 border-b border-grey-light flex justify-start"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-6 w-6 text-blue-400 cursor-pointer"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="{2}"
                          d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
                        />
                      </svg>
                      <svg
                        @click="setGet('document')"
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-6 w-6 text-green-400 cursor-pointer"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="{2}"
                          d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                        />
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="{2}"
                          d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                        />
                      </svg>
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-6 w-6 text-red-400 cursor-pointer"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="{2}"
                          d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636"
                        />
                      </svg>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="my-4 flex justify-between gap-5">
              <div
                class="border-2 border-green-400 bg-green-200 rounded-lg py-2 w-full text-gray-700 text-center"
              >
                Verified
              </div>
              <div
                class="border-2 border-gray-200 rounded-lg py-2 w-full text-gray-700 text-center"
              >
                Not verified
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    user_headers: ["Name", "Position", "Status", "Role"],
    transaction_headers: [
      "ID",
      "Date",
      "Operation",
      "Source",
      "Total",
      "Card",
      "Order",
    ],
    transactions: [
      {
        id: "1029312",
        time: "12:50",
        date: "30 august",
        operation: "payment",
        source: "card",
        total: "1402 rub",
        card: "VISA 7622",
        order: "#996521",
      },
      {
        id: "929321",
        time: "19:37",
        date: "25 august",
        operation: "payment",
        source: "bonus",
        total: "505 rub",
        card: "",
        order: "#896431",
      },
      {
        id: "912837",
        time: "07:50",
        date: "18 august",
        operation: "payment",
        source: "card",
        total: "2020 rub",
        card: "VISA 7622",
        order: "#746411",
      },
      {
        id: "909309",
        time: "12:50",
        date: "16 august",
        operation: "payment",
        source: "card",
        total: "106 rub",
        card: "VISA 7622",
        order: "#711234",
      },
    ],
    users: [
      {
        image:
          "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60",
        name: "Jane Cooper",
        email: "jane.cooper@example.com",
        position: "Sales Manager",
        sphere: "Bank",
        status: "Verified",
        role: "Client",
      },
      {
        image: require(`~/static/img/free-icon-student-4472500.png`),
        name: "Brown Green",
        email: "brown.green@example.com",
        position: "Project Manager",
        sphere: "Oracle",
        status: "Verified",
        role: "Client",
      },
      {
        image: require(`~/static/img/free-icon-teenager-4472497.png`),
        name: "Purple White",
        email: "purple.white@example.com",
        position: "Software Engineer",
        sphere: "Bank",
        status: "Verified",
        role: "Client",
      },
      {
        image: require(`~/static/img/free-icon-teenager-4472485.png`),
        name: "Yellow Black",
        email: "yellow.black@example.com",
        position: "Consultant",
        sphere: "Google",
        status: "Verified",
        role: "Client",
      },
      {
        image: require(`~/static/img/free-icon-teenager-4472494.png`),
        name: "Pinky Green",
        email: "pinky.green@example.com",
        position: "Sales Manager",
        sphere: "Network Service",
        status: "Verified",
        role: "Client",
      },
      {
        image: require(`~/static/img/free-icon-teenager-4472485.png`),
        name: "Redly Blue",
        email: "redly.blue@example.com",
        position: "Car Mechanic",
        sphere: "Auto Service",
        status: "Verified",
        role: "Client",
      },
      {
        image: require(`~/static/img/free-icon-teenager-4472485.png`),
        name: "Browny Black",
        email: "browny.black@example.com",
        position: "DevOps Engineer",
        sphere: "Oracle",
        status: "Verified",
        role: "Client",
      },
      // {
      //   image:
      //     "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60",
      //   name: "Jane Cooper",
      //   email: "jane.cooper@example.com",
      //   position: "Sales Manager",
      //   sphere: "Bank",
      //   status: "Verified",
      //   role: "Client",
      // },
      // {
      //   image:
      //     "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60",
      //   name: "Jane Cooper",
      //   email: "jane.cooper@example.com",
      //   position: "Sales Manager",
      //   sphere: "Bank",
      //   status: "Verified",
      //   role: "Client",
      // },
      // {
      //   image:
      //     "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60",
      //   name: "Jane Cooper",
      //   email: "jane.cooper@example.com",
      //   position: "Sales Manager",
      //   sphere: "Bank",
      //   status: "Verified",
      //   role: "Client",
      // },
    ],
    documents: [
      "Cooper_passport.pdf",
      "Cooper_drivers_license.pdf",
      "Cooper_bank_information.pdf",
      "Cooper_photo_with_passport.png",
    ],
    thisTime: null, // current time
    startDate: null, // start date
    clockStart: null, // start time
    timeOnPage: 0, // user`s time on page
    timeNotOnPage: 0, // user`s time not on page
    countClicks: {
      // object of mouse clicks
      clickLeft: 0,
      clickRight: 0,
      clickMiddle: 0,
    },
    mouseSpeeds: {}, // object of mouse speeds
    mouseDists: {}, // object of mouse dists
    mouseAccelerations: {}, // object of mouse accelerations
    angularCharacteristics: {}, // object of angular characteristics
    timeForMeasure: 10, // every 10 secs ajax request on server with data
    formData: null, // formData object for AJAX
    lastMouseTime: null, // last mouse time
    lastMouseX: null, // last mouse position x
    lastMouseY: null, // last mouse position y
    counter: 0, // counter
    coordinates: {}, // object of coordinates for angular characteristics
    curvatureDistances: {}, // object of curvature distances
    onCriticalArea: {}, // object of critical area
  }),
  methods: {
    setGet: function (slug) {
      axios({
        method: "GET",
        url: "https://192.168.0.16:5000/",
        params: {
          slug: slug,
        },
      })
        .then((response) => console.log(response))
        .catch((error) => console.log(error));
    },
  },
  mounted() {
    // solved problem with "this"
    const ref = this;
    // initial new formData(), new Date()
    const formData = new FormData();
    ref.formData = formData;
    ref.startDate = new Date();
    ref.clockStart = ref.startDate.getTime();

    // critical areas

    const docsOffset = document
      .getElementById("documents")
      .getBoundingClientRect();

    // checking user`s activity on site every second
    setInterval(() => {
      if (!document.hidden) {
        // if page is active
        ref.timeOnPage += 1; // 1 second interval (1000)
        console.log("User is here, time: " + ref.timeOnPage);
      } else {
        // if page is hidden
        ref.timeNotOnPage += 1;
        console.log("User left, time: " + ref.timeNotOnPage);
      }
    }, 1000);
    // listening for mouse moves
    document.addEventListener("mousemove", function (e) {
      ref.counter++;

      ref.coordinates[ref.counter] = {
        x: e.pageX,
        y: e.pageY,
      };

      if (ref.lastMouseTime === null) {
        ref.lastMouseTime = Date.now();
        ref.lastMouseX = e.pageX;
        ref.lastMouseY = e.pageY;
        return;
      }

      // current timestamp
      var now = Date.now();
      // current speeds and accelerations
      var dt = now - ref.lastMouseTime;
      var dx = e.pageX - ref.lastMouseX;
      var dy = e.pageY - ref.lastMouseY;
      var speedX = Math.round((dx / dt) * 100);
      var accelerationX = speedX / dt;
      var speedY = Math.round((dy / dt) * 100);
      var accelerationY = speedY / dt;
      var distanceX = Math.round(dx);
      var distanceY = Math.round(dy);

      // on critical area
      if (
        e.pageX >= docsOffset.left &&
        e.pageX <= docsOffset.left + docsOffset.width &&
        e.pageY >= docsOffset.bottom &&
        e.pageY <= docsOffset.bottom + docsOffset.height
      ) {
        ref.onCriticalArea[now] = true;
      } else {
        ref.onCriticalArea[now] = false;
      }

      if (ref.counter > 3) {
        // 3 vector AC
        var vec3x =
          ref.coordinates[ref.counter - 2].x - ref.coordinates[ref.counter].x;
        var vec3y =
          ref.coordinates[ref.counter - 2].y - ref.coordinates[ref.counter].y;

        // 3 vector AC lenght
        var vec3len = Math.sqrt(Math.pow(vec3x, 2) + Math.pow(vec3y, 2));

        // auxiliary coefficient
        var k =
          ((ref.coordinates[ref.counter - 2].y -
            ref.coordinates[ref.counter].y) *
            (ref.coordinates[ref.counter - 1].x -
              ref.coordinates[ref.counter].x) -
            (ref.coordinates[ref.counter - 2].x -
              ref.coordinates[ref.counter].x) *
              (ref.coordinates[ref.counter - 1].y -
                ref.coordinates[ref.counter].y)) /
          (Math.pow(
            ref.coordinates[ref.counter - 2].y - ref.coordinates[ref.counter].y,
            2
          ) +
            Math.pow(
              ref.coordinates[ref.counter - 2].x -
                ref.coordinates[ref.counter].x,
              2
            ));

        // perpendicular second point (D) coordinates
        var x4 =
          ref.coordinates[ref.counter - 1].x -
          k *
            (ref.coordinates[ref.counter - 2].y -
              ref.coordinates[ref.counter].y);
        var y4 =
          ref.coordinates[ref.counter - 1].y -
          k *
            (ref.coordinates[ref.counter - 2].x -
              ref.coordinates[ref.counter].x);

        // 4 vector BD
        var vec4x = x4 - ref.coordinates[ref.counter - 1].x;
        var vec4y = y4 - ref.coordinates[ref.counter - 1].y;

        // perpendicular vector (BD) lenght
        var vec4len = Math.sqrt(Math.pow(vec4x, 2) + Math.pow(vec4y, 2));

        // curvature distance
        var curDis = vec3len / vec4len;
        ref.curvatureDistances[now] = {
          curDis: curDis,
        };
        // 1 vector AB
        var vec1x =
          ref.coordinates[ref.counter].x - ref.coordinates[ref.counter - 1].x;
        var vec1y =
          ref.coordinates[ref.counter].y - ref.coordinates[ref.counter - 1].y;

        // 2 vector BC
        var vec2x =
          ref.coordinates[ref.counter - 1].x -
          ref.coordinates[ref.counter - 2].x;
        var vec2y =
          ref.coordinates[ref.counter - 1].y -
          ref.coordinates[ref.counter - 2].y;

        // cosine of an angle between vec1 (AB) and vec2 (BC)
        var cosAngle =
          (vec1x * vec2x + vec1y * vec2y) /
          (Math.sqrt(Math.pow(vec1x, 2) + Math.pow(vec1y, 2)) *
            Math.sqrt(Math.pow(vec2x, 2) + Math.pow(vec2y, 2)));

        ref.angularCharacteristics[now] = {
          cosAngle: Math.abs(cosAngle),
        };
      }

      ref.mouseAccelerations[now] = {
        // Math.abs() uses because acceleration can have (-) before
        accelerationX: Math.abs(accelerationX),
        accelerationY: Math.abs(accelerationY),
      };
      ref.mouseSpeeds[now] = {
        speedX: Math.abs(speedX),
        speedY: Math.abs(speedY),
      };
      ref.mouseDists[now] = {
        distanceX: Math.abs(distanceX),
        distanceY: Math.abs(distanceY),
      };
      ref.lastMouseTime = now;
      ref.lastMouseX = e.pageX;
      ref.lastMouseY = e.pageY;
    });
    // listening for mouse clicks
    document.addEventListener("mouseup", function (e) {
      if (typeof e === "object") {
        switch (e.button) {
          case 0:
            ref.countClicks.clickLeft++;
            break;
          case 1:
            ref.countClicks.clickMiddle++;
            break;
          case 2:
            ref.countClicks.clickRight++;
            break;
          default:
            console.log(`Unknown button code: ${e.button}`);
            break;
        }
      }
    });

    // Appending received data in formData object and sending ajax
    setInterval(() => {
      let speed_of_clicks_r = ref.timeOnPage
        ? ref.countClicks.clickRight / ref.timeOnPage
        : 0;
      let speed_of_clicks_m = ref.timeOnPage
        ? ref.countClicks.clickMiddle / ref.timeOnPage
        : 0;
      let speed_of_clicks_l = ref.timeOnPage
        ? ref.countClicks.clickLeft / ref.timeOnPage
        : 0;

      ref.formData.append(
        "speed_of_clicks_r",
        speed_of_clicks_r ? speed_of_clicks_r : 0
      );
      ref.formData.append(
        "speed_of_clicks_l",
        speed_of_clicks_l ? speed_of_clicks_l : 0
      );
      ref.formData.append(
        "speed_of_clicks_m",
        speed_of_clicks_m ? speed_of_clicks_m : 0
      );

      ref.formData.append("time_on_page", ref.timeOnPage);
      ref.formData.append("time_not_on_page", ref.timeNotOnPage);

      ref.formData.append("speeds_of_mouse", JSON.stringify(ref.mouseSpeeds));
      ref.formData.append("dists_of_mouse", JSON.stringify(ref.mouseDists));
      ref.formData.append(
        "accelerations_of_mouse",
        JSON.stringify(ref.mouseAccelerations)
      );
      ref.formData.append(
        "angular_characteristics",
        JSON.stringify(ref.angularCharacteristics)
      );
      ref.formData.append(
        "curvature_distances",
        JSON.stringify(ref.curvatureDistances)
      );
      ref.formData.append(
        "on_critical_area",
        JSON.stringify(ref.onCriticalArea)
      );

      axios({
        method: "POST",
        url: "https://192.168.0.16:5000/",
        data: ref.formData,
        headers: {
          "content-type": "multipart/form-data;",
          "Access-Control-Allow-Origin": "*",
        },
      })
        .then((response) => {
          ref.formData = new FormData();
          ref.mouseAccelerations = {};
          ref.mouseSpeeds = {};
          ref.mouseDists = {};
          ref.angularCharacteristics = {};
          ref.curvatureDistances = {};
          ref.timeNotOnPage = 0;
          ref.timeOnPage = 0;

          if (response.data === "True") {
            // alert("Send user`s data to server");
            console.log("Send user`s data to server!!!");
            console.log(response);
          } else {
            // alert("Something wrong, check console!");
            console.log("Something wrong, check console!");
            console.log(response);
          }
        })
        .catch((error) => console.log(error));
    }, ref.timeForMeasure * 1000);
  },
  layout: "main",
};
</script>

<style></style>
