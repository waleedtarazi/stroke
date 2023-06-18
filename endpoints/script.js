const form = document.querySelector('form');
const alertContainer = document.querySelector('#alert-container');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  // const jsonData ={
  //   "age": 0,
  //   "hypertension": 1,
  //   "heart_disease": 1,
  //   "avg_glucose_level": 0,
  //   "bmi": 0,
  //   "gender": "male",
  //   "ever_married": "yes",
  //   "work_type": "Private",
  //   "residence_type": "Urban",
  //   "smoking_status": "formerly smoked"
  // };


  const jsonData = {
    'age': parseInt(formData.get('age')),
    'hypertension': parseInt(formData.get('hypertension')),
    'heart_disease': parseInt(formData.get('heart-disease')),
    'avg_glucose_level': parseFloat(formData.get('avg-glucose-level')),
    'bmi': parseFloat(formData.get('bmi')),
    'gender': formData.get('gender').toLowerCase(),
    'ever_married': formData.get('ever-married').toLowerCase(),
    'work_type': formData.get('work-type'),
    'residence_type': formData.get('residence-type'),
    'smoking_status': formData.get('smoking-status')
  };




  const response = await fetch('http://localhost:8000/predict_stroke', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(jsonData)
  });
  

  
  const prediction = await response.json();
  
  if (prediction.prediction === 1) {
    alertContainer.innerHTML = '<div class="alert alert-danger">You are at risk of stroke. Please call 911 immediately.</div>';
  } else {
    alertContainer.innerHTML = '<div class="alert alert-success">You are not at risk of stroke. Keep yourself healthy.</div>';
  }
});