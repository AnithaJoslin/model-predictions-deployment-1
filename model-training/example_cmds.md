curl -X POST http://127.0.0.1:8081/predict \
     -H "Content-Type: application/json" \
     -d '{"mean radius": 13.94,"mean area": 594.2,"mean concave points": 0.066,"mean fractal dimension": 0.065,"concavity error": 0.048,"concave points error": 0.0285,"worst radius": 14.62,"worst area": 653.3}'
     
curl -X POST http://127.0.0.1:8081/predict \
     -H "Content-Type: application/json" \
     -d '{
"mean radius": 11.22,
 "mean area": 387.3,
 "mean concave points": 0.007583,
 "mean fractal dimension": 0.0603,
 "concavity error": 0.0033,
 "concave points error": 0.00497,
 "worst radius": 11.98,
 "worst area": 436.1
}'
     
