import uuid

from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models


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
    name = models.CharField(max_length=255)
    brand_model = models.CharField(max_length=255)
    layer_precision = ArrayField(
        models.FloatField(), blank=False, default=list([0.2]))
    hotend_size = ArrayField(
        models.FloatField(), blank=False, default=list([0.4]))
    x_size = models.IntegerField(
        blank=False, validators=[MinValueValidator(1)])
    y_size = models.IntegerField(
        blank=False, validators=[MinValueValidator(1)])
    z_size = models.IntegerField(
        blank=False, validators=[MinValueValidator(1)])
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


DEFAULT_STATUS = 'SOUMIS'
STATUS_IMPRESSION = (
    ('SOUMIS', 'Soumis'),
    ('VALIDE', 'Validé'),
    ('EN ATTENTE', 'En attente'),
    ('REFUSE', 'Refusé'),
    ('IMPRESSION', 'Impression'),
    ('IMPRIME', 'Imprimé')
)


class SubmissionModel(models.Model):
    """
    Chaque soumission doit être enregistrée en base
    Une soumission devrait présenter les champs suivant:
    id_submission (UUIDField)
    designation (CharField, 255)  -- Désignation de l'objet
    about (TextField) - Description de l'impression, raison ...
    stl (BinaryField / FileField ?) -- Fichier Stl
    material (relation) -- Consommable d'impression
    copies (Integer) -- Nombre de même objet à imprimer (0 à 99+)
    submission_date (timestamp)
    update_date (timestamp)
    status (Enum) -- Status du process: Soumis, Accepté, Refusé, En attente, ..
    """
    id_submission = models.UUIDField(primary_key=True, default=uuid.uuid4)
    designation = models.CharField(max_length=255, blank=False)
    about = models.TextField(blank=True)
    stl = models.FileField(blank=False)
    material = models.ForeignKey(
        ConsumableModel, on_delete=models.SET_NULL, null=True)
    copies = models.IntegerField(default=0)
    submission_date = models.DateField(auto_now_add=True)
    submitted_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    update_date = models.DateField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_IMPRESSION, default=DEFAULT_STATUS)


class SlicerParamsModel(models.Model):
    """
    This is generated by admin while treating a print request
    Those parameters are used into the final slicing
    printer (relation) -- Imprimante choisie pour l'impression
    hotend_diameter (Float) -- diamètre de la buse d'impression
    layer_resolution (Integer) -- Hauteur de couche standard
    support (Boolean) -- Nécessite des supports d'impression
    """
    id_params = models.UUIDField(primary_key=True, default=uuid.uuid4)
    submission = models.ForeignKey(
        SubmissionModel, on_delete=models.CASCADE, blank=False)
    printer = models.ForeignKey(
        PrinterModel, on_delete=models.SET_NULL, null=True)
    hotend_diameter = models.FloatField()
    layer_resolution = models.IntegerField()
    support = models.BooleanField(default=False)
