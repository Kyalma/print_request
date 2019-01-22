import uuid

from django.db import models


# Chaque soumission doit être enregistrée en base
# Une soumission devrait présenter les champs suivant:
#   id_submission (Integer)
#   Designation (CharField, 255)  -- Désignation de l'objet
#   about (TextField) - Description de l'impression, raison ...
#   Stl (BinaryField / FileField ?) -- Fichier Stl
#   id_printer (relation) -- Imprimante choisie pour l'impression
#   Hotend_diameter (Integer / Float ?) -- diamètre de la buse d'impression
#   Layer_resolution (Integer) -- Hauteur de couche standard
#   id_material (relation) -- Consommable d'impression
#   Support (Boolean) -- Nécessite des supports d'impression
#   Copies (Integer) -- Nombre de même objet à imprimer (0 à 99+)
#   Submission_date (timestamp)
#   Update_date (timestamp)
#   Status (Enum) -- Status du process: Soumis, Accepté, Refusé, En attente, ..
# La validation des champs suivants doit être fait en pré-publish:
#   id_material, id_printer

DEFAULT_STATUS = '0'
STATUS_IMPRESSION = (
    ('0', 'Soumis'),
    ('1', 'Validé'),
    ('2', 'En attente'),
    ('3', 'Refusé'),
    ('4', 'Impression'),
    ('5', 'Imprimé')
)


class SubmissionModel(models.Model):
    id_submission = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    designation = models.CharField(max_length=255)
    about = models.TextField()
    stl = models.FileField()
    id_printer = models.UUIDField(default=uuid.uuid4)
    hotend_diameter = models.FloatField()
    layer_resolution = models.IntegerField()
    id_material = models.UUIDField(default=uuid.uuid4)
    support = models.BooleanField(default=False)
    copies = models.IntegerField(default=0)
    submission_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    status = models.CharField(
        max_length=1, choices=STATUS_IMPRESSION, default=DEFAULT_STATUS)


# Certains paramètres sont en relation avec les paramètres de l'imprimante
# L'imprimante doit donc avoir une entrée en base, définie selon le modèle:
#   id_printer (IntegerField)
#   Name (CharField, 255)
#   Model (Charfiel, 255)
#   Layer_precision (Array Field, Integer) -- Précision d'une couche en microns
#   Hotend_available (Array Field, Integer) -- Diamètre de buses disponibles
#   X_area_size (Integer) -- Taille X du plateau d'impression en mm
#   Y_area_size (Integer) -- Taille Y du plateau d'impression en mm
#   Z_area_size (Integer) -- Taille Z du plateau d'impression en mm
#   Dual_extruder (Boolean) -- Dispose de deux têtes d'impression
#   Heated_bed (Boolean) -- Dispose d'un plateau chauffant

# Chaque consommable est aussi renseigné en base
#   id_material (Integer)
#   type (CharField, 12) -- Type de consommable (PLA, ABS, ...)
#   variant (Charfield, 255) -- Couleur, Spécial, ...
#   diameter (Integer / Float) -- Diamètre du filament
#   available (boolean) -- En stock ou non
