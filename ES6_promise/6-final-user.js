import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName).then((user) => ({ status: 'fulfilled', value: user }));
  const photoPromise = uploadPhoto(fileName).then(
    () => ({ status: 'fulfilled', value: null }),
    (err) => ({ status: 'rejected', value: `${err.name}: ${err.message}` }),
  );

  return Promise.all([userPromise, photoPromise]);
}
