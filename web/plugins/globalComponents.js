import Vue from 'vue'
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import DatetimePicker from 'vuetify-datetime-picker'
import TopTitle from '~/components/TopTitle'

const components = {
  TopTitle,
  ValidationProvider,
  ValidationObserver
}

Object.entries(components).forEach(([name, component]) => {
  Vue.component(name, component)
})
Vue.use(DatetimePicker)
