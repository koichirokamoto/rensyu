import KerasJS from 'keras-js';

const model = new KerasJS.Model({
  filepath: '',
  gpu: true
});

try {
  await model.ready();
} catch(err) {

}
