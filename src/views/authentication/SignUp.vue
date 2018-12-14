<template>
  <v-app>
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center row>
          <v-flex xs6>
            <v-card dark class="elevation-0 text-sm-left pa-5" color="green">
              <h1>BluePrintIQ</h1>
              <h2>Do you already have an account?</h2>
              <p>That's awesome! you can login by clicking on the button below. To skip this next time, you can ask us
                to remember your login credentials.</p>
              <v-btn outline color="primary" dark class="ma-0">Sign In</v-btn>
            </v-card>
          </v-flex>
          <v-flex xs4 offset-xs1>
            <v-card class="dark--text pa-2 pb-4 elevation-2">
              <v-card-text>
                <h1>Welcome to BluePrintIQ</h1>
                <h3>Create your account by filling the form bellow.</h3>
              </v-card-text>
              <v-card-text class="py-2">
                <v-text-field
                  v-model="email"
                  :rules="emailRules"
                  label="Work Email Address"
                  placeholder="John@compay.com"
                ></v-text-field>
              </v-card-text>
              <v-card-text class="py-2">
                <v-text-field
                  v-model="name"
                  :rules="nameRules"
                  label="Name"
                  placeholder="John Doe"
                ></v-text-field>
              </v-card-text>
              <v-card-text class="py-2">
                <v-text-field
                  v-model="password"
                  :rules="passwordRules"
                  label="Password"
                  placeholder="Enter Password"
                ></v-text-field>
              </v-card-text>
              <v-card-text class="py-2">
                <v-btn block color="primary" dark>Sign Up</v-btn>
              </v-card-text>
            </v-card>

            <p class="copyright dark--text mt-3">
              &copy; 2018 Copyright Company, Inc. &bull; Terms of Service &bull; Privacy Policy
            </p>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'SignUp',
  data: () => ({
    email: '',
    name: '',
    password: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/igm.test(v) || 'E-mail must be valid'
    ],
    nameRules: [
      v => !!v || 'Name is required',
    ],
    passwordRules: [
      v => !!v || 'Password is required',
      v => /\S{8,}/igm.test(v) || 'At least 8 characters',
      v => /(?=.*[A-Z])/igm.test(v) || 'At least 1 character',
      v => /[0-9]/igm.test(v) || 'At least 1 numeric character',
      v => /[!@#$%^&*()]/igm.test(v) || 'At least 1 special character'
    ]
  })
}
</script>

<style lang="scss" scoped>
.copyright {
  text-align: left;
  font-size: 12px;
}
</style>