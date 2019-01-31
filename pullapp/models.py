import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models


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
    """
    Chaque soumission doit être enregistrée en base
    Une soumission devrait présenter les champs suivant:
    id_submission (UUIDField)
    designation (CharField, 255)  -- Désignation de l'objet
    about (TextField) - Description de l'impression, raison ...
    stl (BinaryField / FileField ?) -- Fichier Stl
    id_printer (relation) -- Imprimante choisie pour l'impression
    Hotend_diameter (Float) -- diamètre de la buse d'impression
    Layer_resolution (Integer) -- Hauteur de couche standard
    id_material (relation) -- Consommable d'impression
    support (Boolean) -- Nécessite des supports d'impression
    copies (Integer) -- Nombre de même objet à imprimer (0 à 99+)
    submission_date (timestamp)
    update_date (timestamp)
    status (Enum) -- Status du process: Soumis, Accepté, Refusé, En attente, ..
    """
    id_submission = models.UUIDField(primary_key=True, default=uuid.uuid4)
    designation = models.CharField(max_length=255, blank=False)
    about = models.TextField(blank=True)
    stl = models.FileField(blank=False)
    id_material = models.ForeignKey(
        ConsumableModel, on_delete=models.SET_NULL, blank=False)
    copies = models.IntegerField(default=0)
    # misc
    submission_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    status = models.CharField(
        max_length=1, choices=STATUS_IMPRESSION, default=DEFAULT_STATUS)
    # Printer parameters: Done by admin
    id_printer = models.ForeignKey(
        PrinterModel, on_delete=models.SET_NULL, blank=False)
    hotend_diameter = models.FloatField()
    layer_resolution = models.IntegerField()
    support = models.BooleanField(default=False)


class PrinterModel(models.Model):
    """
    Certains paramètres sont en relation avec les paramètres de l'imprimante
    L'imprimante doit donc avoir une entrée en base, définie selon le modèle:
    id_printer (UUIDField)
    name (CharField, 255)
    brand_model (Charfiel, 255)
    Layer_precision (Array Field, Integer) -- Précision d'une couche en microns
    Hotend_size (Array Field, Float) -- Diamètre de buses disponibles
    x_size (Integer) -- Taille X du plateau d'impression en mm
    y_size (Integer) -- Taille Y du plateau d'impression en mm
    z_size (Integer) -- Taille Z du plateau d'impression en mm
    dual_extruder (Boolean) -- Dispose de deux têtes d'impression
    heated_bed (Boolean) -- Dispose d'un plateau chauffant
    """
    id_printer = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_lenth=255)
    brand_model = models.Charfield(max_lenth=255)
    layer_precision = ArrayField(
        models.FloatField(), blank=False, default=[0.2])
    hotend_size = ArrayField(models.FloatField(), blank=False, default=[0.4])
    x_size = models.IntegerField(blank=False)
    y_size = models.IntegerField(blank=False)
    z_size = models.IntegerField(blank=False)
    dual_extruder = models.BooleanField(default=False)
    heated_bed = models.BooleanField(default=False)


class ConsumableModel(models.Model):
    """
    Chaque consommable est aussi renseigné en base
    id_material (UUIDField)
    consumable (CharField, 32) -- Type de consommable (PLA, ABS, ...)
    variant (Charfield, 255) -- Couleur, Spécial, ...
    diameter (Float) -- Diamètre du filament
    available (Boolean) -- En stock ou non
    """
    id_material = models.UUIDField(primary_key=True, default=uuid.uuid4)
    consumable = models.CharField(max_length=32, blank=False)
    variant = models.CharField(max_length=255, blank=False)
    diameter = models.FloatField(blank=False)
    available = models.BooleanField(default=True)
