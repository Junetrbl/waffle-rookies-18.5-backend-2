source ~/.bash_profile

cd ~/waffle-rookies-18.5-backend-2/

echo "Git Pull for recent changes..."
git pull

echo "Python virtual environment activating..."
cd ~/.pyenv/versions/waffle-backend/
source ./bin/activate

echo "Installing base python packages for the app..."
cd ~/waffle-rookies-18.5-backend-2/
pip install -r requirements.txt

echo "Migration to database..."
cd ~/waffle-rookies-18.5-backend-2/waffle_backend/
python manage.py makemigrations
python manage.py migrate

echo "Check --deploy..."
python manage.py check --deploy

echo "Update a symbolic link to the nginx conf file in sites-enabled..."
cd /etc/nginx/sites-enabled/
sudo rm waffle-backend.conf
sudo ln -s /etc/nginx/sites-available/waffle-backend.conf /etc/nginx/sites-enabled/waffle-backend.conf

echo "Restart Uswgi..."
uwsgi --ini /home/ec2-user/waffle-rookies-18.5-backend-2/waffle_backend/waffle-backend_uwsgi.ini

echo "Restart Nginx..."
sudo nginx -t

sudo service nginx restart

echo "Done!"
