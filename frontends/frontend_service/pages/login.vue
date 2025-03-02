<template>
  <div class="mt-5 p-3 shadow rounded">
    <div class="p-1 rounded text-center">
<!--      <img-->
<!--          src="https://static.vecteezy.com/system/resources/previews/015/815/200/original/kindness-icon-design-free-vector.jpg"-->
<!--          alt="Kindness"-->
<!--      />-->
      <h6 class="text-center primary-color">Login to feel better</h6>
    </div>

    <hr/>
    <UForm :schema="schema" :state="state" class="space-y-4" @submit="onSubmit">
    <UFormGroup label="Email" name="email">
      <UInput v-model="state.email" required/>
    </UFormGroup>

    <UFormGroup label="Password" name="password">
      <UInput v-model="state.password" type="password" required />
    </UFormGroup>

    <UButton type="submit" class="btn custom-btn w-100">
      Submit
    </UButton>
      <p class="text-center mt-3">
        You don't have an account ?
        <NuxtLink class="primary-color" to="/register">Register</NuxtLink>
      </p>

     <UAlert v-if="formError != ''" type="error" class="mt-3 text-center" :description="formError">
      {{ formError }}
    </UAlert>
  </UForm>
  </div>
</template>

<script lang="ts" setup>

definePageMeta({
  middleware: 'auth'
})
import {useAuthStore, type UserPayloadInterface} from "~/store/auth";
import { z } from 'zod';
const {authenticateUser} = useAuthStore();
const router = useRouter();

const schema = z.object({
  email: z.string().email('Invalid email'),
  password: z.string().min(2, 'Must be at least 2 characters')
})


const formError = ref('');
const state = reactive({
  email : '',
  password: ''
})

const onSubmit = async() => {
  const userPayload : UserPayloadInterface = { email: state.email, password: state.password };
  try {
    console.log("userPayload", userPayload);
    await authenticateUser(userPayload);
  }
  catch (e) {
    formError.value = e.message;
  }
}

</script>
