from django.db import models


class InstinctLog(models.Model):
    view_method = models.CharField(max_length=50, null=True, blank=True)
    path = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    request = models.JSONField(null=True, blank=True)
    response = models.JSONField(null=True, blank=True)
    error_message = models.CharField(max_length=255, null=True, blank=True)
    status_code = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    response_time = models.DecimalField(
        max_digits=4, decimal_places=4, null=True, blank=True
    )
    request_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.view_method} - {self.path}"

    class Meta:
        db_table = "internal_instinct_log"
