from flask import Flask , render_template , request
import logic 

app = Flask(__name__)

@app.route('/',methods=['GET','POST']
           def index():
             display_result = None
            
             if request.method=='POST':
               
               input_value = request.form.get('mass')
               
               display_result = logic.calculate_force(input_value)
             
             return render_template('index.html',result = display_result)
          
           if __name__ == '__main__':
             app.run(debug=True)  
