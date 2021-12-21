<template>
  <div class="container flex justify-start">
    <div class="my-4 mx-4 overflow-x-auto w-full">
      <div class="align-middle inline-block min-w-full">
        <div class="shadow overflow-hidden sm:rounded-lg">
          <table
            class="min-w-full divide-y divide-purple-300 border-solid border-2 border-purple-200"
          >
            <thead class="bg-purple-200">
              <tr>
                <th
                  v-for="transaction_header in transaction_headers"
                  :key="transaction_header.id"
                  scope="col"
                  class="px-6 py-3 text-xs font-medium text-gray-600 uppercase tracking-wider text-center"
                >
                  {{ transaction_header }}
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-purple-200">
              <tr v-for="transaction in transactions" :key="transaction.id">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div
                    class="text-sm text-indigo-600 hover:text-indigo-900 cursor-pointer text-center"
                  >
                    #{{ transaction.id }}
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-center">
                    <div class="">
                      <div class="text-sm font-medium text-black">
                        {{ transaction.time }}
                      </div>
                      <div class="text-sm text-gray-600">
                        {{ transaction.date }}
                      </div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-800 text-center">
                    {{ transaction.operation }}
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-center">
                  <span
                    class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-purple-100 text-gray-800"
                  >
                    {{ transaction.source }}
                  </span>
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-gray-600 text-center"
                >
                  {{ transaction.total }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-center text-sm font-medium"
                >
                  <div
                    class="text-indigo-600 hover:text-indigo-900 cursor-pointer"
                  >
                    {{ transaction.card }}
                  </div>
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-indigo-600 hover:text-indigo-900 cursor-pointer text-center"
                >
                  {{ transaction.order }}
                </td>
                <td
                  class="text-indigo-600 hover:text-indigo-900 cursor-pointer px-6 py-4 whitespace-nowrap text-sm text-gray-600 text-center"
                >
                  {{ transaction.user }}
                </td>
                <td class="py-4 px-6 flex justify-evenly">
                  <!-- <svg
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
                  </svg> -->
                  <a :href="'transactions/' + transaction.id"
                    ><svg
                      @click="setGet('transaction')"
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-6 w-6 text-green-400 mt-2 cursor-pointer"
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
                      /></svg
                  ></a>
                  <!-- <svg
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
                  </svg> -->
                </td>
              </tr>
              <!-- More transactions... -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  head() {
    return {
      title: "Orders",
      meta: [{ hid: "description", name: "description", content: "Test desc" }],
    };
  },
  layout: "main",
  data: () => ({
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
        user: "Jane Cooper",
      },
      {
        id: "1029311",
        time: "12:50",
        date: "30 august",
        operation: "payment",
        source: "bonus",
        total: "333 rub",
        card: "",
        order: "#896431",
        user: "Brown Green",
      },
      {
        id: "1029310",
        time: "12:49",
        date: "30 august",
        operation: "payment",
        source: "bonus",
        total: "505 rub",
        card: "",
        order: "#746411",
        user: "Purple White",
      },
      {
        id: "1029309",
        time: "12:49",
        date: "30 august",
        operation: "payment",
        source: "card",
        total: "7592 rub",
        card: "VISA 7188",
        order: "#711234",
        user: "Yellow Black",
      },
      {
        id: "1029312",
        time: "12:49",
        date: "30 august",
        operation: "payment",
        source: "card",
        total: "205 rub",
        card: "VISA 2102",
        order: "#996521",
        user: "Pinky Green",
      },
      {
        id: "1029311",
        time: "12:47",
        date: "30 august",
        operation: "payment",
        source: "bonus",
        total: "750 rub",
        card: "",
        order: "#896431",
        user: "Redly Blue",
      },
      {
        id: "1029310",
        time: "12:46",
        date: "30 august",
        operation: "payment",
        source: "bonus",
        total: "590 rub",
        card: "",
        order: "#746411",
        user: "Browny Black",
      },
      {
        id: "1029309",
        time: "12:46",
        date: "30 august",
        operation: "refill",
        source: "card",
        total: "1500 rub",
        card: "VISA 8125",
        order: "#711234",
        user: "Browny Black",
      },
      {
        id: "1029312",
        time: "12:45",
        date: "30 august",
        operation: "refill",
        source: "card",
        total: "2000 rub",
        card: "VISA 7622",
        order: "#996521",
        user: "Jane Cooper",
      },
    ],
    transaction_headers: [
      "ID",
      "Date",
      "Operation",
      "Source",
      "Total",
      "Card",
      "Order",
      "User",
      "View",
    ],
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
  created() {},
  mounted() {},
};
</script>

<style scoped></style>
