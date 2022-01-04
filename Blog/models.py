from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image



class Post(models.Model): 
    werkstoffnummer = models.CharField(max_length=100)
    werkstoffbezeichnung = models.CharField(max_length=100)
    gruppe = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    #title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    Iron_Fe = models.CharField(max_length=100, default='', blank=True)
    Carbon_C = models.CharField(max_length=100, default='', blank=True)
    Cobalt_Co = models.CharField(max_length=100, default='', blank=True)
    Nickel_Ni = models.CharField(max_length=100, default='', blank=True)
    Copper_Cu = models.CharField(max_length=100, default='', blank=True)
    Zinc_Zn = models.CharField(max_length=100, default='', blank=True)
    Mananese_Mn = models.CharField(max_length=100, default='', blank=True)
    Chromuium_Cr = models.CharField(max_length=100, default='', blank=True)
    Vanadium_V = models.CharField(max_length=100, default='', blank=True)
    Titaniun_Ti = models.CharField(max_length=100, default='', blank=True)
    Cadmium_Cd = models.CharField(max_length=100, default='', blank=True)
    Silver_Ag = models.CharField(max_length=100, default='', blank=True)
    Palladium_Pb = models.CharField(max_length=100, default='', blank=True)
    Rhodium_Rh = models.CharField(max_length=100, default='', blank=True)
    Molydbenum_Mo = models.CharField(max_length=100, default='', blank=True)
    Niobium_Nb = models.CharField(max_length=100, default='', blank=True)
    Zirconium_Zr = models.CharField(max_length=100, default='', blank=True)
    Yttrium_Y = models.CharField(max_length=100, default='', blank=True)
    Tungesten_W = models.CharField(max_length=100, default='', blank=True)
    Aluminium_Al = models.CharField(max_length=100, default='', blank=True)
    Boron_B = models.CharField(max_length=100, default='', blank=True)
    Gallium_Ga = models.CharField(max_length=100, default='', blank=True)
    Indium_In = models.CharField(max_length=100, default='', blank=True)
    Lead_Pb = models.CharField(max_length=100, default='', blank=True)
    Silicon_Si = models.CharField(max_length=100, default='', blank=True)
    Tin_Sn = models.CharField(max_length=100, default='', blank=True)
    Nitrogen_N = models.CharField(max_length=100, default='', blank=True)
    Phosphorus_P = models.CharField(max_length=100, default='', blank=True)
    Sulfur_S = models.CharField(max_length=100, default='', blank=True)
    Notes = models.CharField(max_length=5000, default='', blank=True)
    Technetium_Tc = models.CharField(max_length=100, default='', blank=True)

    Hardness_HV = models.CharField(max_length=1000, default='', blank=True)
    Hardness_HRC = models.CharField(max_length=1000, default='', blank=True)
    Hardness_HBW = models.CharField(max_length=1000, default='', blank=True)
    files_Hardness = models.FileField(blank=True, upload_to="chapters/%Y/%m/%D", default='no_data.html')

    Tensile_Strength_Rm = models.CharField(max_length=1000, default='', blank=True)
    Streckgrenze_Rp = models.CharField(max_length=1000, default='', blank=True)
    Streckgrenze_ReH = models.CharField(max_length=1000, default='', blank=True)
    Streckgrenze_ReL = models.CharField(max_length=1000, default='', blank=True)
    Tensile_Stretch_A = models.CharField(max_length=1000, default='', blank=True)
    Gleichmaßdehnung_Ag = models.CharField(max_length=1000, default='', blank=True)
    files_Tensile = models.FileField(blank=True, upload_to="chapters/%Y/%m/%D", default='no_data.html')

    Kerbschlagarbeit = models.CharField(max_length=1000, default='', blank=True)
    Temperatur = models.CharField(max_length=1000, default='', blank=True)
    files_Charpy = models.FileField(blank=True, upload_to="chapters/%Y/%m/%D", default='no_data.html')

    EModul = models.CharField(max_length=1000, default='', blank=True)
    files_Modulus = models.FileField(blank=True, upload_to="chapters/%Y/%m/%D", default='no_data.html')

    Density = models.CharField(max_length=100, default='', blank=True)
    files_Density = models.FileField(blank=True, upload_to="chapters/%Y/%m/%D", default='no_data.html')



    Probe = models.CharField(max_length=1000, default='', blank=True)
    Gefüge_Beschreibung = models.CharField(max_length=1000, default='', blank=True)
    files_Metallo = models.FileField(blank=True, upload_to="chapters/%Y/%m/%D", default='no_data.html')
    Wärmebehandlung = models.CharField(max_length=1000, default='', blank=True)
    Ätzung = models.CharField(max_length=1000, default='', blank=True)
    Gefüge_Aufnhame= models.ImageField(blank=True, upload_to="chapters/%Y/%m/%D", default='no_data.jpg')

     
    def __str__(self):
        return self.werkstoffnummer
        

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
        
    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.Gefüge_Aufnhame.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.Gefüge_Aufnhame.path)




