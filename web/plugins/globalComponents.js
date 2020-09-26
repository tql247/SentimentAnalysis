import Vue from 'vue'
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import VueKatex from 'vue-katex'
import TopTitle from '~/components/TopTitle'
import 'katex/dist/katex.min.css'

const components = {
  TopTitle,
  ValidationProvider,
  ValidationObserver
}

Object.entries(components).forEach(([name, component]) => {
  Vue.component(name, component)
})
Vue.use(VueKatex)
