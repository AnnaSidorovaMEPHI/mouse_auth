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
                  v-for="order_header in order_headers"
                  :key="order_header.id"
                  scope="col"
                  class="px-6 py-3 text-xs font-medium text-gray-600 uppercase tracking-wider text-center"
                >
                  {{ order_header }}
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-purple-200">
              <tr v-for="order in orders" :key="order.id">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-purple-900">{{ order.id }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="ml-4">
                      <div class="text-sm font-medium text-purple-900">
                        {{ order.time }}
                      </div>
                      <div class="text-sm text-gray-600">{{ order.date }}</div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-purple-900">{{ order.service }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span
                    class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-purple-100 text-gray-800"
                  >
                    {{ order.status }}
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                  {{ order.address }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
                >
                  <div class="text-indigo-600 hover:text-indigo-900">
                    {{ order.car }}
                  </div>
                </td>
              </tr>
              <!-- More orders... -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="w-2/5 my-4">
      <div
        class="sm:rounded-lg material-card bg-white border-solid border-2 border-purple-200"
      >
        <div class="px-6 py-4">
          <div class="font-bold text-xl tracking-wide">Order #996521</div>
          <div class="my-3">
            <span
              class="px-4 py-2 inline-flex text-lg leading-5 font-semibold rounded-full bg-purple-300 text-black"
            >
              Сompleted
            </span>
          </div>
          <div
            class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase flex justify-start"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 mr-2"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fillRule="evenodd"
                d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z"
                clipRule="evenodd"
              />
            </svg>
            Moscow, Kaluzhskaya street, 8
          </div>
          <div
            class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase flex justify-start"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 mr-2"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fillRule="evenodd"
                d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z"
                clipRule="evenodd"
              />
            </svg>
            Moscow, Tverskaya street, 12A
          </div>
          <div class="mt-6">
            <a
              class="tracking-wider uppercase font-bold text-purple-700 bg-purple-100 rounded p-2 inline-block"
              href="#"
              >Information</a
            >
            <!-- <a
              class="tracking-wider uppercase font-bold text-purple-700 hover:bg-purple-100 rounded p-2 inline-block"
              href="#"
              >Payment Information</a
            > -->
          </div>
        </div>
        <div class="bg-white rounded">
          <table class="text-center w-full">
            <thead>
              <tr>
                <th
                  class="py-2 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark"
                >
                  Client
                </th>
                <th
                  class="py-1 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark"
                >
                  Payment
                </th>
                <th
                  class="py-2 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark"
                >
                  Time
                </th>
              </tr>
            </thead>
            <tbody>
              <tr class="hover:bg-grey-lighter">
                <td class="px-6 mb-4 flex justify-start">
                  <div class="flex-shrink-0 h-10 w-10">
                    <img
                      src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60"
                      alt=""
                      class="w-10 h-10 rounded-full object-cover content-center border-4 border-purple"
                    />
                  </div>
                  <div class="ml-4">
                    <div class="text-sm font-medium text-purple-900">
                      Jane Cooper
                    </div>
                    <div class="text-sm text-gray-600">
                      jane.cooper@example.com
                    </div>
                  </div>
                </td>
                <td class="px-6">
                  <span
                    class="px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-200 text-gray-800"
                  >
                    Processing
                  </span>
                </td>
                <td class="px-6 text-purple-500">1:57:92</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: "Orders",
      meta: [{ hid: "description", name: "description", content: "Test desc" }],
    };
  },
  layout: "main",
  data: () => ({
    orders: [
      {
        id: "#996521",
        time: "12:50",
        date: "30 august",
        service: "Comfort",
        status: "Complited",
        address: "Moscow, Kaluzhskaya street, 8",
        car: "Kia Rio",
      },
      {
        id: "#996520",
        time: "12:50",
        date: "30 августа",
        service: "Comfort",
        status: "Active",
        address: "Moscow, Kaluzhskaya street, 8",
        car: "Kia Rio",
      },
      {
        id: "#996519",
        time: "12:50",
        date: "30 августа",
        service: "Comfort",
        status: "Active",
        address: "Moscow, Kaluzhskaya street, 8",
        car: "Kia Rio",
      },
      {
        id: "#996518",
        time: "12:50",
        date: "30 августа",
        service: "Comfort",
        status: "Active",
        address: "Moscow, Kaluzhskaya street, 8",
        car: "Kia Rio",
      },
      {
        id: "#996517",
        time: "12:50",
        date: "30 августа",
        service: "Comfort",
        status: "Active",
        address: "Moscow, Kaluzhskaya street, 8",
        car: "Kia Rio",
      },
      {
        id: "#996516",
        time: "12:50",
        date: "30 августа",
        service: "Comfort",
        status: "Active",
        address: "Moscow, Kaluzhskaya street, 8",
        car: "Kia Rio",
      },
      {
        id: "#996515",
        time: "12:50",
        date: "30 августа",
        service: "Comfort",
        status: "Active",
        address: "Moscow, Kaluzhskaya street, 8",
        car: "Kia Rio",
      },
      {
        id: "#996514",
        time: "12:50",
        date: "30 августа",
        service: "Comfort",
        status: "Active",
        address: "Moscow, Kaluzhskaya street, 8",
        car: "Kia Rio",
      },
      {
        id: "#996513",
        time: "12:50",
        date: "30 августа",
        service: "Comfort",
        status: "Active",
        address: "Moscow, Kaluzhskaya street, 8",
        car: "Kia Rio",
      },
      {
        id: "#996512",
        time: "12:50",
        date: "30 августа",
        service: "Comfort",
        status: "Active",
        address: "Moscow, Kaluzhskaya street, 8",
        car: "Kia Rio",
      },
      {
        id: "#996511",
        time: "12:50",
        date: "30 августа",
        service: "Comfort",
        status: "Active",
        address: "Moscow, Kaluzhskaya street, 8",
        car: "Kia Rio",
      },
      {
        id: "#996510",
        time: "12:50",
        date: "30 августа",
        service: "Comfort",
        status: "Active",
        address: "Moscow, Kaluzhskaya street, 8",
        car: "Kia Rio",
      },
    ],
    order_headers: ["№", "Date", "Service", "Status", "From", "Car"],
  }),
  methods: {},
  mounted() {},
};
</script>

<style scoped></style>
