"# Site_de_stiri_cu_Python"
Pentru a putea rula site-ul, sunt necesare urmatoarele programe / comenzi:

- Download Anaconda cu Puthon versiunea 3.x

- Download Atom IDE

- Creare virtual-environment de django cu urmatoarea secventa (scrisa in command prompt): conda create --name myDjangoEnv django

- In urmatorul pas activati vm-ul creat anterior, cu urmatoarea comanda (scrisa in command prompt): activate myDjangoEnv

- De indata ce vm-ul a fost activat, introduceti urmatoarea comanda: conda install django

- Tot in vm-ul de django (acesta trebuie sa fie activat) instalati Pillow folosind comanda: pip install Pillow


Urmatoarele comenzi sunt necesare pentru deschiderea site-ului (rularea efectiva), toate scrise in command prompt:

- navigati in folderul cu siteul, folosind: cd numele_folderului

- deschideti directorul cu 'project-ul', acesta fiind urmatorul folder din interior: cd nume_forder_urmator

- executati urmatoarea comanda pentru ca site-ul sa fie activ: python manage.py runserver

- ca sa vizualizati site-ul, copiati adresa localhost-ului ce s-a deschis anterior (ex: http://127.0.0.1:8000/)
