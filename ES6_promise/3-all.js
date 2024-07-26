import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
  .then((values) => {
    console.log(values[0], values[1])
  }), () => {
    console.log('Signup system offline')
  }
}
