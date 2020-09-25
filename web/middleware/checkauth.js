export default function({ store, $auth, redirect }) {
  if ($auth.loggedIn) {
    console.log('login')
  } else {
    console.log('chua login')
    // return this.redirect('/login')
  }
}
