from django.db import models


STATES = (
        ('fl', 'Florida'),
        ('hi', 'Hawaii'),
        ('ga', 'Georgia'),
        ('cl', 'California'),
        ('mt', 'Montana'),
        ('nj', 'New Jersey'),
        ('nm', 'New Mexico'),
        ('ny', 'New York'),
    )


STATUS = (
        ('1', 'Initial submission'),
        ('2', 'Rate confirmed'),
        ('3', 'Client submission'),
        ('4', 'Interview'),
        ('5', 'Project confirmed'),
        ('6', 'On project'),
        ('7', 'Rejected by vendor'),
        ('8', 'Rejected in interview'),
        ('9', 'Offer rejected'),
    )

class Common(models.Model):
    """Model definition for Common class sharing common fields to inherited classes"""

    consultant_name = models.CharField(max_length=100, null=True, blank=True)
    availability_date = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True


class Consultant(Common):
    """Model definition for Consultant."""

    employment_type = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        """Meta definition for Consultant."""

        verbose_name = 'Consultant'
        verbose_name_plural = 'Consultants'


    def __str__(self): 
        return self.consultant_name


class ProspectConsultant(Common):
    """Model definition for ProspectConsultant."""

    technology = models.CharField(max_length=100, null=True, blank=True)
    trainer = models.CharField(max_length=100, null=True, blank=True)
    training_status = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        """Meta definition for ProspectConsultant."""

        verbose_name = 'ProspectConsultant'
        verbose_name_plural = 'ProspectConsultants'


    def __str__(self): 
        return self.consultant_name


class Benchlist(Common):
    """Model definition for Benchlist."""

    title = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    visa = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    bench_days = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        """Meta definition for Benchlist."""

        verbose_name = 'Benchlist'
        verbose_name_plural = 'Benchlist consultants'
    

    def __str__(self): 
        return self.consultant_name


class Submission(models.Model):
    """Model definition for Submission."""

    

    class Meta:
        """Meta definition for Submission."""

        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'


    consultant_name = models.CharField(max_length=100)
    date_of_submission = models.DateField()
    job_title = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    rate_confirmation = models.BooleanField(default=False)
    client = models.CharField(max_length=100)
    client_city = models.CharField(max_length=100)
    client_state = models.CharField(max_length=100, choices=STATES)
    vendor_company = models.CharField(max_length=100)
    vendor_recruiter_contact = models.CharField(max_length=100)
    vendor_location = models.CharField(max_length=100)
    submission_status = models.CharField(max_length=100, choices=STATUS, default=1)
    reason = models.TextField(max_length=100, null=True, blank=True)
    note = models.TextField(null=True, blank=True)


    def __str__(self):
        """Unicode representation of Submission."""
        return self.consultant_name
