from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=100)


class Part(models.Model):
    name = models.CharField(max_length=100)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)


class Workstation(models.Model):
    name = models.CharField(max_length=100)
    materials = models.ManyToManyField(Material)

    # workflow_set


class Workflow(models.Model):
    name = models.CharField(max_length=100)
    workstations = models.ManyToManyField(Workstation)


class Sequence(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    parts = models.ManyToManyField(Part)


# class Job(models.Model):
#     part = models.ForeignKey(Part, on_delete=models.CASCADE)
#     workstation = models.ForeignKey(Workstation, on_delete=models.CASCADE)
