<template>
  <div class="flex justify-start w-full ml-80">
    <div class="w-1/3 mx-2">
      <div class="font-bold text-xl tracking-wide mt-6 text-center">
        Transaction #{{ id }}
      </div>
      <div
        class="sm:rounded-lg material-card border-solid border border-purple-light bg-white text-center my-4 shadow-lg"
      >
        <div class="my-5 flex justify-between mx-8">
          <div class="text-center">
            <h1 class="text-gray-500 mb-2">Source</h1>
            <span
              class="px-4 py-2 inline-flex text-lg leading-5 font-semibold rounded-full bg-purple-100 text-gray-800"
            >
              card
            </span>
          </div>
          <div class="text-center">
            <h1 class="text-gray-500 mb-2">Operation</h1>
            <span
              class="px-4 py-2 inline-flex text-lg leading-5 font-semibold rounded-full bg-purple-100 text-gray-800"
            >
              payment
            </span>
          </div>
          <div class="text-center">
            <h1 class="text-gray-500 mb-3">Order</h1>
            <p class="text-xl text-blue-800">#996521</p>
          </div>
        </div>
        <div class="my-5 flex justify-between mx-8">
          <div class="ml-12">
            <h1 class="text-gray-500 mb-2 text-center">Status</h1>
            <button
              class="py-2 px-4 rounded-full text-white text-lg font-semibold inline-flex leading-5 font-semibold bg-green-100 text-gray-800"
            >
              Complited
            </button>
          </div>
          <div class="text-center mr-10">
            <h1 class="text-gray-500 mb-3">Date</h1>
            <div class="text-center">
              <div class="flex justify-between">
                <div class="text-xl text-gray-700 mr-2">12:50</div>
                <div class="text-xl text-gray-500">30 Августа</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="my-4 text-center">
        <div
          class="sm:rounded-lg material-card bg-white border-solid border border-purple-light shadow-lg"
        >
          <div class="px-6 py-4 flex justify-between">
            <img
              src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60"
              alt=""
              class="w-20 h-20 rounded-full object-cover content-center mt-5 ml-20 border-4 border-purple"
            />
            <div class="mr-20 mt-5">
              <div class="font-bold text-xl tracking-wide">Jane Cooper</div>
              <div class="my-3">
                <span
                  class="px-4 py-2 inline-flex text-lg leading-5 font-semibold rounded-full bg-purple-100 text-black"
                >
                  verified
                </span>
              </div>
            </div>
          </div>
          <div class="bg-white">
            <div class="my-5 flex justify-between mx-8">
              <div class="text-left">
                <h1 class="text-gray-500">Email</h1>
                <p class="text-xl text-gray-800">jane.cooper@example.com</p>
              </div>
              <div class="text-left">
                <h1 class="text-gray-500">Registered</h1>
                <p class="text-xl text-gray-800">14.10.2017</p>
              </div>
            </div>
            <div class="my-5 flex justify-between mx-8">
              <div class="text-left">
                <h1 class="text-gray-500">Orders</h1>
                <p class="text-xl text-gray-800">78</p>
              </div>
              <div class="text-left">
                <h1 class="text-gray-500">Phone</h1>
                <p class="text-xl text-gray-800">+79075004030</p>
              </div>
              <div class="text-left">
                <h1 class="text-gray-500">Role</h1>
                <p class="text-xl text-gray-800">Client</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="bg-white my-4 mx-6 text-center">
      <div class="font-bold text-xl tracking-wide my-2">Card`s Information</div>
      <div class="flex justify-between">
        <div
          class="mt-2 bg-white border border-purple-light shadow-lg rounded-lg"
        >
          <table class="text-center w-full">
            <tbody>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Card
                </td>
                <td
                  class="text-blue-900 py-4 px-10 border-b border-grey-light underline cursor-pointer"
                >
                  VISA 7622
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Type
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Personal
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Status
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Active
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  BIN
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  123124
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Cardowner
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  JANE COOPER
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Valid until
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  10/2022
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Gateway
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  alfa
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Bank
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  ALFA BANK
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Type
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Debit
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Level
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Gold
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Country
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Russian Federation
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td class="text-grey-900 py-4 px-10 cursor-pointer">UID</td>
                <td class="text-blue-900 underline py-4 px-10 cursor-pointer">
                  b12312350921358902b2134n2n2
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- <div
          class="mt-2 mx-5 bg-white border border-purple-light shadow-lg rounded-lg"
        >
          <table class="text-center w-full">
            <tbody>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Card
                </td>
                <td
                  class="text-blue-900 py-4 px-10 border-b border-grey-light underline cursor-pointer"
                >
                  MasterCard 1488
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Type
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Personal
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Status
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Active
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  BIN
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  456232
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Cardowner
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  JANE COOPER
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Valid until
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  10/2020
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Gateway
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  alfa
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Bank
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  TINKOFF CREDIT SYSTEMS BANK
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Type
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Credit
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Level
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Gold
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Country
                </td>
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  Russian Federation
                </td>
              </tr>
              <tr class="hover:bg-grey-lighter">
                <td
                  class="text-grey-900 py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  UID
                </td>
                <td
                  class="text-blue-900 underline py-4 px-10 border-b border-grey-light cursor-pointer"
                >
                  a676867485786s67087e878e
                </td>
              </tr>
            </tbody>
          </table>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    id: null,
  }),
  mounted() {},
  created() {
    this.id = this.$route.params.id;
  },
  methods: {},
  layout: "main",
};
</script>

<style></style>
