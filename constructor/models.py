from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True, help_text="Product Category Name")
    key = models.CharField(max_length=250, unique=True, help_text="Product Category Key")
    order = models.IntegerField(default=1, )

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}-{self.key}"


class ImageField(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Image Name")
    image = models.ImageField(upload_to='uploads/body')
    x_point = models.IntegerField()
    y_point = models.IntegerField()
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}-{self.name}"


class Body(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Body Name")

    # Body Start

    body_view = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='body_view', )
    body_first_section = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='body_first_section',
                                           blank=True, null=True)
    body_second_section = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='body_second_section',
                                            blank=True, null=True)
    body_third_section = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='body_third_section',
                                           blank=True, null=True)
    collar = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='collar', blank=True, null=True)
    hem = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hem', blank=True, null=True)
    right_sleeve = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='r_sleeve', blank=True,
                                     null=True)
    left_sleeve = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='l_sleeve', blank=True,
                                    null=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"

        #########     Hat Start    ##########

#
# class HatFront(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text="HatFront")
#     hat_full_body_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_full_body_front',
#                                             null=True, blank=True)
#     hat_dot_left_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_dot_left_front', null=True,
#                                      blank=True)
#     hat_dot_right_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_dot_right_front', null=True,
#                                       blank=True)
#     hat_upper_part_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_upper_part_front', null=True,
#                                        blank=True)
#     hat_lower_part_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_lower_part_front', null=True,
#                                        blank=True)
#     hat_top_button_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_top_button_front', null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class HatLeft(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text="HatLeft")
#     hat_full_body_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_full_body_left',
#                                            null=True, blank=True)
#
#     hat_dot_left_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_dot_left_left', null=True,
#                                      blank=True)
#     hat_dot_right_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_dot_right_left', null=True,
#                                       blank=True)
#     hat_upper_part_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_upper_part_left', null=True,
#                                        blank=True)
#     hat_lower_part_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_lower_part_left', null=True,
#                                        blank=True)
#     hat_top_button_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_top_button_left', null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class HatRight(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text="HatRight")
#     hat_full_body_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_full_body_right',
#                                             null=True, blank=True)
#
#     hat_dot_left_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_dot_left_right', null=True,
#                                      blank=True)
#     hat_dot_right_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_dot_right_right', null=True,
#                                       blank=True)
#     hat_upper_part_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_upper_part_right', null=True,
#                                        blank=True)
#     hat_lower_part_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_lower_part_right', null=True,
#                                        blank=True)
#     hat_top_button_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_top_button_right', null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class HatBack(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text="HatBack")
#     hat_full_body_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_full_body_back',
#                                            null=True, blank=True)
#
#     hat_dot_left_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_dot_left_back', null=True,
#                                      blank=True)
#     hat_dot_right_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_dot_right_back', null=True,
#                                       blank=True)
#     hat_upper_part_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_upper_part_back', null=True,
#                                        blank=True)
#     hat_lower_strip_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hat_lower_strip_back', null=True,
#                                         blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#         #########     Hat End    ##########
#
#         #########     Hoodie Start    ##########
#
#
# class HoodieFront(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text="Hoodie Front")
#
#     # Cap Start
#     cap_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='cap_left', blank=True, null=True)
#     cap_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='cap_right', blank=True, null=True)
#     cap_inner_mid = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='cap_inner_mid', blank=True,
#                                       null=True)
#     cap_inner_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='cap_inner_left', blank=True,
#                                        null=True)
#     cap_inner_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='cap_inner_right',
#                                         blank=True, null=True)
#     cap_inner_bottom = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='cap_inner_bottom',
#                                          blank=True, null=True)
#     # Cap Ends
#
#     # Hood Strips
#     hood_left_strip = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_left_strip', null=True,
#                                         blank=True)
#     hood_right_strip = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_right_strip',
#                                          null=True, blank=True)
#     # Hood Strips
#
#     # Zip Start
#     zip = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='zip', blank=True, null=True)
#     # Zip End
#
#     # Hood Top Start
#     hood_top = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_top', blank=True, null=True)
#     hood_top_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_top_left', blank=True,
#                                       null=True)
#     hood_top_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_top_right', blank=True,
#                                        null=True)
#     # Hood Top End
#
#     # Hood Mid Start
#     hood_mid = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_mid', blank=True, null=True)
#     hood_mid_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_mid_left', blank=True,
#                                       null=True)
#     hood_mid_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_mid_right', blank=True,
#                                        null=True)
#     # Hood Mid End
#
#     # Hood Bottom Start
#     hood_bottom = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_bottom', blank=True,
#                                     null=True)
#     hood_bottom_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_bottom_left',
#                                          blank=True, null=True)
#     hood_bottom_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_bottom_right',
#                                           blank=True, null=True)
#     # Hood Bottom End
#
#     # Hood Hem Start
#     hood_hem_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_hem_left', null=True,
#                                       blank=True)
#     hood_hem_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_hem_right', null=True,
#                                        blank=True)
#     # Hood Hem End
#
#     # Hood LeftSleeve Front Start
#     hood_left_sleeve_full = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='hood_left_sleeve_full', null=True, blank=True)
#     hood_left_sleeve_top = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_left_sleeve_top',
#                                              null=True, blank=True)
#     hood_left_sleeve_mid = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_left_sleeve_mid',
#                                              null=True, blank=True)
#     hood_left_sleeve_bottom = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                 related_name='hood_left_sleeve_bottom', null=True, blank=True)
#     hood_left_sleeve_cuff = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='hood_left_sleeve_cuff', null=True, blank=True)
#     hood_left_sleeve_cuff_strips = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                      related_name='hood_left_sleeve_cuff_strips', null=True, blank=True)
#     # Hood LeftSleeve Front End
#
#     # Hood RightSleeve Front Start
#     hood_right_sleeve_full = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                related_name='hood_right_sleeve_full', null=True, blank=True)
#     hood_right_sleeve_top = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='hood_right_sleeve_top',
#                                               null=True, blank=True)
#     hood_right_sleeve_mid = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='hood_right_sleeve_mid',
#                                               null=True, blank=True)
#     hood_right_sleeve_bottom = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                  related_name='hood_right_sleeve_bottom', null=True, blank=True)
#     hood_right_sleeve_cuff = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                related_name='hood_right_sleeve_cuff', null=True, blank=True)
#     hood_right_sleeve_cuff_strips = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                       related_name='hood_right_sleeve_cuff_strips', null=True,
#                                                       blank=True)
#
#     # Hood RightSleeve Front End
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class HoodieLeft(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text="Hoodie Left")
#
#     # Hoodie Mid Part Start
#     mid_full_body_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                   related_name='mid_full_body_hoodie_left', null=True, blank=True)
#     mid_top_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='mid_top_hoodie_left',
#                                             null=True, blank=True)
#     mid_mid_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='mid_mid_hoodie_left',
#                                             null=True, blank=True)
#     mid_bottom_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                related_name='mid_bottom_hoodie_left', null=True, blank=True)
#     mid_cuff_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='mid_cuff_hoodie_left',
#                                              null=True, blank=True)
#     mid_cuff_strips_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                     related_name='mid_cuff_strips_hoodie_left', null=True, blank=True)
#     # Hoodie Mid Part End
#
#     # Hoodie LeftSleeve Start
#     left_full_body_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                    related_name='left_full_body_hoodie_left',
#                                                    null=True, blank=True)
#     left_top_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_top_hoodie_left',
#                                              null=True,
#                                              blank=True)
#     left_mid_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_mid_hoodie_left',
#                                              null=True,
#                                              blank=True)
#     left_bottom_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                 related_name='left_bottom_hoodie_left',
#                                                 null=True, blank=True)
#     left_cuff_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='left_cuff_hoodie_left', null=True,
#                                               blank=True)
#     left_cuff_strips_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                      related_name='left_cuff_strips_hoodie_left', null=True, blank=True)
#     # Hoodie LeftSleeve End
#
#     # Hoodie RightSleeve Start
#     right_full_body_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                     related_name='right_full_body_hoodie_left',
#                                                     null=True, blank=True)
#     right_top_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='right_top_hoodie_left', null=True,
#                                               blank=True)
#     right_mid_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='right_mid_hoodie_left', null=True,
#                                               blank=True)
#     right_bottom_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                  related_name='right_bottom_hoodie_left',
#                                                  null=True, blank=True)
#     right_cuff_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                related_name='right_cuff_hoodie_left',
#                                                null=True,
#                                                blank=True)
#     right_cuff_strips_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                       related_name='right_cuff_strips_hoodie_left', null=True,
#                                                       blank=True)
#     # Hoodie RightSleeve End
#
#     # Hoodie BottomSleeve Start
#     bottom_full_body_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                      related_name='bottom_full_body_hoodie_left',
#                                                      null=True, blank=True)
#     bottom_top_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                related_name='bottom_top_hoodie_left',
#                                                null=True,
#                                                blank=True)
#     bottom_mid_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                related_name='bottom_mid_hoodie_left',
#                                                null=True,
#                                                blank=True)
#     bottom_bottom_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                   related_name='bottom_bottom_hoodie_left',
#                                                   null=True, blank=True)
#     bottom_cuff_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                 related_name='bottom_cuff_hoodie_left',
#                                                 null=True,
#                                                 blank=True)
#     bottom_cuff_strips_hoodie_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                        related_name='bottom_cuff_strips_hoodie_left', null=True,
#                                                        blank=True)
#
#     # Hoodie BottomSleeve End
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class HoodieRight(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text="Hoodie Left")
#
#     # Hoodie Mid Part Start
#     mid_full_body_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                    related_name='mid_full_body_hoodie_right', null=True, blank=True)
#     mid_top_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='mid_top_hoodie_right',
#                                              null=True, blank=True)
#     mid_mid_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='mid_mid_hoodie_right',
#                                              null=True, blank=True)
#     mid_bottom_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                 related_name='mid_bottom_hoodie_right', null=True, blank=True)
#     mid_cuff_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='mid_cuff_hoodie_right', null=True, blank=True)
#     mid_cuff_strips_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                      related_name='mid_cuff_strips_hoodie_right', null=True, blank=True)
#     # Hoodie Mid Part End
#
#     # Hoodie LeftSleeve Start
#     left_full_body_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                     related_name='left_full_body_hoodie_right',
#                                                     null=True, blank=True)
#     left_top_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='left_top_hoodie_right', null=True,
#                                               blank=True)
#     left_mid_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='left_mid_hoodie_right', null=True,
#                                               blank=True)
#     left_bottom_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                  related_name='left_bottom_hoodie_right',
#                                                  null=True, blank=True)
#     left_cuff_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                related_name='left_cuff_hoodie_right', null=True,
#                                                blank=True)
#     left_cuff_strips_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                       related_name='left_cuff_strips_hoodie_right', null=True,
#                                                       blank=True)
#     # Hoodie LeftSleeve End
#
#     # Hoodie RightSleeve Start
#     right_full_body_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                      related_name='right_full_body_hoodie_right',
#                                                      null=True, blank=True)
#     right_top_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                related_name='right_top_hoodie_right', null=True,
#                                                blank=True)
#     right_mid_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                related_name='right_mid_hoodie_right', null=True,
#                                                blank=True)
#     right_bottom_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                   related_name='right_bottom_hoodie_right',
#                                                   null=True, blank=True)
#     right_cuff_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                 related_name='right_cuff_hoodie_right',
#                                                 null=True,
#                                                 blank=True)
#     right_cuff_strips_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                        related_name='right_cuff_strips_hoodie_right', null=True,
#                                                        blank=True)
#     # Hoodie RightSleeve End
#
#     # Hoodie BottomSleeve Start
#     bottom_full_body_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                       related_name='bottom_full_body_hoodie_right',
#                                                       null=True, blank=True)
#     bottom_top_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                 related_name='bottom_top_hoodie_right',
#                                                 null=True,
#                                                 blank=True)
#     bottom_mid_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                 related_name='bottom_mid_hoodie_right',
#                                                 null=True,
#                                                 blank=True)
#     bottom_bottom_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                    related_name='bottom_bottom_hoodie_right',
#                                                    null=True, blank=True)
#     bottom_cuff_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                  related_name='bottom_cuff_hoodie_right',
#                                                  null=True,
#                                                  blank=True)
#     bottom_cuff_strips_hoodie_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                         related_name='bottom_cuff_strips_hoodie_right', null=True,
#                                                         blank=True)
#
#     # Hoodie BottomSleeve End
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class HoodieBack(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text="Hoodie Front")
#
#     # Cap Back Start
#     cap_left_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='cap_left_back', blank=True,
#                                       null=True)
#     cap_right_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='cap_right_back', blank=True,
#                                        null=True)
#     # Cap Back Ends
#
#     # Hood Top Back Start
#     hood_top_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_top_back', blank=True,
#                                       null=True)
#     hood_top_left_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_top_left_back',
#                                            blank=True,
#                                            null=True)
#     hood_top_right_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_top_right_back',
#                                             blank=True,
#                                             null=True)
#     # Hood Top Back End
#
#     # Hood Mid Back Start
#     hood_mid_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_mid_back', blank=True,
#                                       null=True)
#     hood_mid_left_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_mid_left_back',
#                                            blank=True,
#                                            null=True)
#     hood_mid_right_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_mid_right_back',
#                                             blank=True,
#                                             null=True)
#     # Hood Mid Back End
#
#     # Hood Bottom Back Start
#     hood_bottom_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_bottom_back',
#                                          blank=True,
#                                          null=True)
#     hood_bottom_left_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='hood_bottom_left_back',
#                                               blank=True, null=True)
#     hood_bottom_right_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                related_name='hood_bottom_right_back',
#                                                blank=True, null=True)
#     # Hood Bottom Back End
#
#     # Hood Hem Back Start
#     hood_hem_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='hood_hem_back',
#                                       null=True,
#                                       blank=True)
#     # Hood Hem Back End
#
#     # Hood LeftSleeve Back Start
#     hood_left_sleeve_full_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                    related_name='hood_left_sleeve_full_back', null=True, blank=True)
#     hood_left_sleeve_top_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                   related_name='hood_left_sleeve_top_back',
#                                                   null=True, blank=True)
#     hood_left_sleeve_mid_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                   related_name='hood_left_sleeve_mid_back',
#                                                   null=True, blank=True)
#     hood_left_sleeve_bottom_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                      related_name='hood_left_sleeve_bottom_back', null=True, blank=True)
#     hood_left_sleeve_cuff_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                    related_name='hood_left_sleeve_cuff_back', null=True, blank=True)
#     hood_left_sleeve_cuff_strips_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                           related_name='hood_left_sleeve_cuff_strips_back', null=True,
#                                                           blank=True)
#     # Hood LeftSleeve Back End
#
#     # Hood RightSleeve Back Start
#     hood_right_sleeve_full_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                     related_name='hood_right_sleeve_full_back', null=True, blank=True)
#     hood_right_sleeve_top_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                    related_name='hood_right_sleeve_top_back',
#                                                    null=True, blank=True)
#     hood_right_sleeve_mid_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                    related_name='hood_right_sleeve_mid_back',
#                                                    null=True, blank=True)
#     hood_right_sleeve_bottom_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                       related_name='hood_right_sleeve_bottom_back', null=True,
#                                                       blank=True)
#     hood_right_sleeve_cuff_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                     related_name='hood_right_sleeve_cuff_back', null=True, blank=True)
#     hood_right_sleeve_cuff_strips_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                            related_name='hood_right_sleeve_cuff_strips_back', null=True,
#                                                            blank=True)
#
#     # Hood RightSleeve Back End
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#         #########     Hoodie End    ##########
#
#         #########     Bag Start     ##########
#
#         #########     Hoodie Start    ##########
#
#         #########     Bag Start    ##########
#
#
# class BagFront(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Bag Front')
#     bag_handle_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='bag_handle_front',
#                                          null=True, blank=True)
#     bag_full_front_body = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='bag_full_front_body',
#                                             null=True, blank=True)
#     bag_top_front_body = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='bag_top_front_body',
#                                            null=True, blank=True)
#     bag_mid_front_body = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='bag_mid_front_body',
#                                            null=True, blank=True)
#     bag_bottom_front_body = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='bag_bottom_front_body', null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class BagBack(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Bag Back')
#     bag_handle_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='bag_handle_back', null=True,
#                                         blank=True)
#     bag_full_back_body = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='bag_full_back_body',
#                                            null=True, blank=True)
#     bag_top_back_body = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='bag_top_back_body',
#                                           null=True, blank=True)
#     bag_mid_back_body = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='bag_mid_back_body',
#                                           null=True, blank=True)
#     bag_bottom_back_body = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='bag_bottom_back_body',
#                                              null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
class PantFront(TimeStampedModel):
    name = models.CharField(max_length=250, help_text='Pant Front')

    # Pant Body Start
    pant_upper_waist_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                               related_name='pant_upper_waist_front', null=True, blank=True)
    pant_lower_waist_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                               related_name='pant_lower_waist_front', null=True, blank=True)
    pant_thai_left_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='pant_thai_left_front',
                                             null=True, blank=True)
    pant_thai_right_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                              related_name='pant_thai_right_front', null=True, blank=True)
    pant_knees_left_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                              related_name='pant_knees_left_front', null=True, blank=True)
    pant_knees_right_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                               related_name='pant_knees_right_front', null=True, blank=True)
    pant_bottom_left_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                               related_name='pant_bottom_left_front', null=True, blank=True)
    pant_bottom_right_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                                related_name='pant_bottom_right_front', null=True, blank=True)
    # Pant Body End

    # Pant Pockets Start
    pant_pocket_left_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                               related_name='pant_pocket_left_front', null=True, blank=True)
    pant_pocket_right_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                                related_name='pant_pocket_right_front', null=True, blank=True)

    # Pant Pocket End

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"
#
#
class PantBack(TimeStampedModel):
    name = models.CharField(max_length=250, help_text='Pant Back')

    # Pant Body Back Start
    pant_upper_waist_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                              related_name='pant_upper_waist_back', null=True, blank=True)
    pant_lower_waist_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                              related_name='pant_lower_waist_back', null=True, blank=True)
    pant_thai_left_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='pant_thai_left_back',
                                            null=True, blank=True)
    pant_thai_right_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='pant_thai_right_back',
                                             null=True, blank=True)
    pant_knees_left_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='pant_knees_left_back',
                                             null=True, blank=True)
    pant_knees_right_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                              related_name='pant_knees_right_back', null=True, blank=True)
    pant_bottom_left_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                              related_name='pant_bottom_left_back', null=True, blank=True)
    pant_bottom_right_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                               related_name='pant_bottom_right_back', null=True, blank=True)
    # Pant Body Back End

    # Pant Pockets Back Start
    pant_pocket_left_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                              related_name='pant_pocket_left_back', null=True, blank=True)
    pant_pocket_right_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                               related_name='pant_pocket_right_back', null=True, blank=True)

    # Pant Pocket Back End

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"
#
#
class Apron(TimeStampedModel):
    name = models.CharField(max_length=250, help_text='Apron')

    display_image = models.ImageField(upload_to='uploads/display')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    collar_strip = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='collar_strip')
    collar_strip_side = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='collar_strip_side',
                                          null=True, blank=True)
    bukkle = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='bukkle', null=True, blank=True)
    body = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='body')
    left_strip = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_strip', null=True,
                                   blank=True)
    right_strip = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='right_strip', null=True,
                                    blank=True)
    pocket = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='pocket', null=True, blank=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"
#
#
# class TowelFront(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Towel Front')
#     towel_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='towel_front', null=True,
#                                     blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class TowelBack(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Towel Back')
#     towel_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='towel_back', null=True,
#                                    blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
class VestFront(TimeStampedModel):
    name = models.CharField(max_length=250, help_text='VestFront')
    # display_image = models.ImageField(upload_to='uploads/display')
    collar_vest = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='collar_vest', null=True,
                                    blank=True)
    zip_vest = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='zip_vest', null=True, blank=True)
    vest_top_full = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_top_full', null=True,
                                      blank=True)
    vest_top_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_top_left', null=True,
                                      blank=True)
    vest_top_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_top_right', null=True,
                                       blank=True)
    vest_mid_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_mid_left', null=True,
                                      blank=True)
    vest_mid_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_mid_right', null=True,
                                       blank=True)
    vest_bottom_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_bottom_left',
                                         null=True, blank=True)
    vest_bottom_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_bottom_right',
                                          null=True, blank=True)
    vest_pocket_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_pocket_left',
                                         null=True, blank=True)
    vest_pocket_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_pocket_right',
                                          null=True, blank=True)
    vest_hem = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_hem', null=True, blank=True)
    vest_left_sleeve = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_left_sleeve',
                                         null=True, blank=True)
    vest_right_sleeve = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_right_sleeve',
                                          null=True, blank=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class VestBack(TimeStampedModel):
    name = models.CharField(max_length=250, help_text='VestBack')

    collar_vest_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='collar_vest_back', null=True,
                                         blank=True)
    vest_full_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_full_back', null=True,
                                       blank=True)
    vest_top_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_top_back', null=True,
                                      blank=True)
    vest_mid_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_mid_back', null=True,
                                      blank=True)
    vest_bottom_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_bottom_back',
                                         null=True, blank=True)
    vest_pocket_left_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                              related_name='vest_pocket_left_back', null=True, blank=True)
    vest_pocket_right_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                               related_name='vest_pocket_right_back', null=True, blank=True)
    vest_hem_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='vest_hem_back', null=True,
                                      blank=True)
    vest_left_sleeve_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                              related_name='vest_left_sleeve_back', null=True, blank=True)
    vest_right_sleeve_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
                                               related_name='vest_right_sleeve_back', null=True, blank=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"

#
# class BaseBallJacket_Front(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Base Ball Jacket Front')
#
#     # Front Body Start
#     base_b_jac_front_body = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                               related_name='base_b_jac_front_body', null=True, blank=True)
#     # Front Body End
#
#     # Front Collar Start
#     base_b_jac_front_collar = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                 related_name='base_b_jac_front_collar', null=True, blank=True)
#     base_b_jac_front_collar_inner = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                       related_name='base_b_jac_front_collar_inner', null=True,
#                                                       blank=True)
#     # Front Collar End
#
#     # Front Hem Start
#     base_b_jac_front_hem = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_front_hem',
#                                              null=True, blank=True)
#     base_b_jac_front_hem_strips = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                     related_name='base_b_jac_front_hem_strips', null=True, blank=True)
#     base_b_jac_front_hem_mid = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                  related_name='base_b_jac_front_hem_mid', null=True, blank=True)
#     # Front Hem End
#
#     # Front Button Body Start
#     base_b_jac_front_button_body = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                      related_name='base_b_jac_front_button_body', null=True, blank=True)
#     base_b_jac_front_button_hem = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                     related_name='base_b_jac_front_button_hem', null=True, blank=True)
#     # Front Button Body End
#
#     # Front Pockets Start
#     base_b_jac_left_pocket_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                      related_name='base_b_jac_left_pocket', null=True, blank=True)
#     base_b_jac_right_pocket_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                       related_name='base_b_jac_right_pocket', null=True, blank=True)
#     # Front Pockets End
#
#     # Front Left Sleeve Start
#     base_b_jac_left_sleeve_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                      related_name='base_b_jac_left_sleeve', null=True, blank=True)
#     # Front Left Sleeve End
#
#     # Front Left Sleeve Cuff Start
#     base_b_jac_left_cuff_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                    related_name='base_b_jac_left_cuff_front', null=True, blank=True)
#     base_b_jac_left_cuff_front_strips = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                           related_name='base_b_jac_left_cuff_front_strips', null=True,
#                                                           blank=True)
#     # Front Left Sleeve Cuff End
#
#     # Front Right Sleeve Start
#     base_b_jac_right_sleeve_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                       related_name='base_b_jac_right_sleeve_front', null=True,
#                                                       blank=True)
#     # Front Right Sleeve End
#
#     # Front Right Sleeve Cuff Start
#     base_b_jac_right_cuff_front = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                     related_name='base_b_jac_right_cuff_front', null=True, blank=True)
#     base_b_jac_right_cuff_front_strips = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                            related_name='base_b_jac_right_cuff_front_strips', null=True,
#                                                            blank=True)
#
#     # Front Right Sleeve Cuff End
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class BaseBallJacket_Left(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Base Ball Jacket Left')
#
#     #Base Ball Jacket Mid Left Start
#     base_b_jac_mid_body_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_mid_body_left', null=True, blank=True)
#     base_b_jac_mid_cuff_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_mid_cuff_left', null=True, blank=True)
#     base_b_jac_mid_cuff_strips_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_mid_cuff_strips_left', null=True, blank=True)
#     # Base Ball Jacket Mid Left End
#
#     #Base Ball Jacket Left Sleeve Left Start
#     base_b_jac_left_body_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_left_body_left', null=True, blank=True)
#     base_b_jac_left_cuff_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_left_cuff_left', null=True, blank=True)
#     base_b_jac_left_cuff_strips_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_left_cuff_strips_left', null=True, blank=True)
#     #Base Ball Jacket Left Sleeve Left End
#
#     # Base Ball Jacket Right Sleeve Left Start
#     base_b_jac_right_body_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                   related_name='base_b_jac_right_body_left', null=True, blank=True)
#     base_b_jac_right_cuff_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                   related_name='base_b_jac_right_cuff_left', null=True, blank=True)
#     base_b_jac_right_cuff_strips_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                          related_name='base_b_jac_right_cuff_strips_left', null=True,
#                                                          blank=True)
#     # Base Ball Jacket Right Sleeve Left End
#
#     # Base Ball Jacket Bottom Sleeve Left Start
#     base_b_jac_bottom_body_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                    related_name='base_b_jac_bottom_body_left', null=True, blank=True)
#     base_b_jac_bottom_cuff_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                    related_name='base_b_jac_bottom_cuff_left', null=True, blank=True)
#     base_b_jac_bottom_cuff_strips_left = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                           related_name='base_b_jac_bottom_cuff_strips_left', null=True,
#                                                           blank=True)
#     # Base Ball Jacket Right Sleeve Left End
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class BaseBallJacket_Right(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Base Ball Jacket Right')
#
#     #Base Ball Jacket Mid Left Start
#     base_b_jac_mid_body_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_mid_body_right', null=True, blank=True)
#     base_b_jac_mid_cuff_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_mid_cuff_right', null=True, blank=True)
#     base_b_jac_mid_cuff_strips_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_mid_cuff_strips_right', null=True, blank=True)
#     # Base Ball Jacket Mid Left End
#
#     #Base Ball Jacket Left Sleeve Left Start
#     base_b_jac_left_body_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_left_body_right', null=True, blank=True)
#     base_b_jac_left_cuff_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_left_cuff_right', null=True, blank=True)
#     base_b_jac_left_cuff_strips_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_left_cuff_strips_right', null=True, blank=True)
#     #Base Ball Jacket Left Sleeve Left End
#
#     # Base Ball Jacket Right Sleeve Left Start
#     base_b_jac_right_body_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                   related_name='base_b_jac_right_body_right', null=True, blank=True)
#     base_b_jac_right_cuff_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                   related_name='base_b_jac_right_cuff_right', null=True, blank=True)
#     base_b_jac_right_cuff_strips_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                          related_name='base_b_jac_right_cuff_strips_right', null=True,
#                                                          blank=True)
#     # Base Ball Jacket Right Sleeve Left End
#
#     # Base Ball Jacket Bottom Sleeve Left Start
#     base_b_jac_bottom_body_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                    related_name='base_b_jac_bottom_body_right', null=True, blank=True)
#     base_b_jac_bottom_cuff_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                    related_name='base_b_jac_bottom_cuff_right', null=True, blank=True)
#     base_b_jac_bottom_cuff_strips_right = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                           related_name='base_b_jac_bottom_cuff_strips_right', null=True,
#                                                           blank=True)
#     # Base Ball Jacket Right Sleeve Left End
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class BaseBallJacket_Back(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Base Ball Jacket Back')
#
#     #Back Collar Start
#     base_b_jac_collar_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_collar_back', null=True, blank=True)
#     base_b_jac_collar_strips_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_collar_strips_back', null=True, blank=True)
#     #Back Collar End
#
#     #Back Body Start
#     base_b_jac_body_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_body_back', null=True, blank=True)
#     #Back Body End
#
#     #Back Hem Start
#     base_b_jac_hem_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_hem_back', null=True, blank=True)
#     base_b_jac_hem_strips_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_hem_strips_back', null=True, blank=True)
#     #Back Hem End
#
#     #Back Left Sleeve Start
#     base_b_jac_left_sleeve_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_left_sleeve_back', null=True, blank=True)
#     base_b_jac_left_cuff_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_left_cuff_back', null=True, blank=True)
#     base_b_jac_left_cuff_strip_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_jac_left_cuff_strip_back', null=True, blank=True)
#     #Back Left Sleeve End
#
#     # Back Right Sleeve Start
#     base_b_jac_right_sleeve_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                     related_name='base_b_jac_right_sleeve_back', null=True, blank=True)
#     base_b_jac_right_cuff_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                   related_name='base_b_jac_right_cuff_back', null=True, blank=True)
#     base_b_jac_right_cuff_strip_back = models.ForeignKey(ImageField, on_delete=models.CASCADE,
#                                                         related_name='base_b_jac_right_cuff_strip_back', null=True,
#                                                         blank=True)
#     # Back Right Sleeve End
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class BaseBallShirt_Front(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Base Ball Shirt Front')
#
#     base_b_shirt_body_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_body_front', null=True, blank=True)
#     base_b_shirt_neck_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_neck_front', null=True, blank=True)
#     base_b_shirt_left_sleeve_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_left_sleeve_front', null=True, blank=True)
#     base_b_shirt_right_sleeve_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_right_sleeve_front', null=True, blank=True)
#     base_b_shirt_button_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_button_front', null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class BaseBallShirt_Left(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Base Ball Shirt Left')
#
#     base_b_shirt_mid_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_mid_left', null=True, blank=True)
#     base_b_shirt_left_sleeve_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_left_sleeve_left', null=True, blank=True)
#     base_b_shirt_right_sleeve_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_right_sleeve_left', null=True, blank=True)
#     base_b_shirt_bottom_sleeve_left = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_bottom_sleeve_left', null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class BaseBallShirt_Right(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Base Ball Shirt Right')
#
#     base_b_shirt_mid_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_mid_right', null=True, blank=True)
#     base_b_shirt_left_sleeve_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_left_sleeve_right', null=True, blank=True)
#     base_b_shirt_right_sleeve_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_right_sleeve_right', null=True, blank=True)
#     base_b_shirt_bottom_sleeve_right = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_bottom_sleeve_right', null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class BaseBallShirt_Back(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Base Ball Shirt Back')
#
#     base_b_shirt_body_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_body_back', null=True, blank=True)
#     base_b_shirt_left_sleeve_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_left_sleeve_back', null=True, blank=True)
#     base_b_shirt_right_sleeve_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='base_b_shirt_right_sleeve_back', null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class TankTop_Front(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Tank Top Front')
#
#     tank_collar_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_collar_front', null=True, blank=True)
#     tank_collar_inner_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_collar_inner_front', null=True, blank=True)
#     tank_top_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_top_front', null=True, blank=True)
#     tank_mid_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_mid_front', null=True, blank=True)
#     tank_bottom_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_bottom_front', null=True, blank=True)
#     tank_left_sleeve_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_left_sleeve_front', null=True, blank=True)
#     tank_right_sleeve_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_right_sleeve_front', null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class TankTop_Back(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Tank Top Back')
#
#     tank_collar_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_collar_back', null=True, blank=True)
#     tank_top_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_top_back', null=True, blank=True)
#     tank_mid_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_mid_back', null=True, blank=True)
#     tank_bottom_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_bottom_back', null=True, blank=True)
#     tank_left_sleeve_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_left_sleeve_back', null=True, blank=True)
#     tank_right_sleeve_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='tank_right_sleeve_back', null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class CoachJacket_Front(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Coach Jacket Front')
#
#     coach_jac_body_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='coach_jac_body_front', null=True, blank=True)
#
#     #Coach Jacket Collar Start
#     coach_jac_collar_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='coach_jac_collar_front', null=True, blank=True)
#     coach_jac_collar_inner_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='coach_jac_collar_inner_front', null=True, blank=True)
#     # Coach Jacket Collar End
#
#     coach_jac_button_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='coach_jac_button_front', null=True, blank=True)
#
#     #Coach Jacket Pocket Start
#     coach_jac_left_pocket_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='coach_jac_left_pocket_front', null=True, blank=True)
#     coach_jac_right_pocket_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='coach_jac_right_pocket_front', null=True, blank=True)
#     # Coach Jacket Pocket Start
#
#     coach_jac_hem_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='coach_jac_hem_front', null=True, blank=True)
#
#     #Coach Jacket Sleeve Start
#     coach_jac_left_sleeve_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='coach_jac_left_sleeve_front', null=True, blank=True)
#     coach_jac_right_sleeve_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='coach_jac_right_sleeve_front', null=True, blank=True)
#     coach_jac_left_cuff_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='coach_jac_left_cuff_front', null=True, blank=True)
#     coach_jac_right_cuff_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='coach_jac_right_cuff_front', null=True, blank=True)
#     #Coach Jacket Sleeve End
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class CoachJacket_Left(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Coach Jacket Left')
#
#     coach_jac_mid_body_left = models.ForeignKey(ImageField, related_name='coach_jac_mid_body_left', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_left_body_left = models.ForeignKey(ImageField, related_name='coach_jac_left_body_left', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_right_body_left = models.ForeignKey(ImageField, related_name='coach_jac_right_body_left', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_bottom_body_left = models.ForeignKey(ImageField, related_name='coach_jac_bottom_body_left', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_mid_cuff_left = models.ForeignKey(ImageField, related_name='coach_jac_mid_cuff_left', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_left_cuff_left = models.ForeignKey(ImageField, related_name='coach_jac_left_cuff_left', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_right_cuff_left = models.ForeignKey(ImageField, related_name='coach_jac_right_cuff_left', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_bottom_cuff_left = models.ForeignKey(ImageField, related_name='coach_jac_bottom_cuff_left', on_delete=models.CASCADE, null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class CoachJacket_Right(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Coach Jacket Right')
#
#     coach_jac_mid_body_right = models.ForeignKey(ImageField, related_name='coach_jac_mid_body_right', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_left_body_right = models.ForeignKey(ImageField, related_name='coach_jac_left_body_right', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_right_body_right = models.ForeignKey(ImageField, related_name='coach_jac_right_body_right', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_bottom_body_right = models.ForeignKey(ImageField, related_name='coach_jac_bottom_body_right', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_mid_cuff_right = models.ForeignKey(ImageField, related_name='coach_jac_mid_cuff_right', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_left_cuff_right = models.ForeignKey(ImageField, related_name='coach_jac_left_cuff_right', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_right_cuff_right = models.ForeignKey(ImageField, related_name='coach_jac_right_cuff_right', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_bottom_cuff_right = models.ForeignKey(ImageField, related_name='coach_jac_bottom_cuff_right', on_delete=models.CASCADE, null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class CoachJacket_Back(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Coach Jacket Back')
#
#     coach_jac_body_back = models.ForeignKey(ImageField, related_name='coach_jac_body_back', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_collar_back = models.ForeignKey(ImageField, related_name='coach_jac_collar_back', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_left_sleeve_back = models.ForeignKey(ImageField, related_name='coach_jac_left_sleeve_back', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_right_sleeve_back = models.ForeignKey(ImageField, related_name='coach_jac_right_sleeve_back', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_hem_back = models.ForeignKey(ImageField, related_name='coach_jac_hem_back', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_left_cuff_back = models.ForeignKey(ImageField, related_name='coach_jac_left_cuff_back', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_right_cuff_back = models.ForeignKey(ImageField, related_name='coach_jac_left_cuff_back', on_delete=models.CASCADE, null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class BomberJacket_Front(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Bomber Jacket Front')
#
#     coach_jac_body_front = models.ForeignKey(ImageField, related_name='coach_jac_body_front', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_collar_front = models.ForeignKey(ImageField, related_name='coach_jac_collar_front', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_collar_inner_front = models.ForeignKey(ImageField, related_name='coach_jac_collar_inner_front', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_left_pocket_front = models.ForeignKey(ImageField, related_name='coach_jac_left_pocket_front', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_right_pocket_front = models.ForeignKey(ImageField, related_name='coach_jac_right_pocket_front', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_left_sleeve_front = models.ForeignKey(ImageField, related_name='coach_jac_left_sleeve_front', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_right_sleeve_front = models.ForeignKey(ImageField, related_name='coach_jac_right_sleeve_front', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_left_cuff_front = models.ForeignKey(ImageField, related_name='coach_jac_left_cuff_front', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_right_cuff_front = models.ForeignKey(ImageField, related_name='coach_jac_right_cuff_front', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_right_sleeve_design_front = models.ForeignKey(ImageField, related_name='coach_jac_right_sleeve_design_front', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_hem_front = models.ForeignKey(ImageField, related_name='coach_jac_hem_front', on_delete=models.CASCADE, null=True, blank=True)
#     coach_jac_zip_front = models.ForeignKey(ImageField, related_name='coach_jac_zip_front', on_delete=models.CASCADE, null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class BomberJacket_Left(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Bomber Jacket Left')
#
#     bomber_jac_mid_body_left = models.ForeignKey(ImageField, related_name='bomber_jac_mid_body_left', null=True, blank=True)
#     bomber_jac_left_body_left = models.ForeignKey(ImageField, related_name='bomber_jac_left_body_left', null=True, blank=True)
#     bomber_jac_right_body_left = models.ForeignKey(ImageField, related_name='bomber_jac_right_body_left', null=True, blank=True)
#     bomber_jac_bottom_body_left = models.ForeignKey(ImageField, related_name='bomber_jac_bottom_body_left', null=True, blank=True)
#     bomber_jac_left_cuff_left = models.ForeignKey(ImageField, related_name='bomber_jac_left_cuff_left', null=True, blank=True)
#     bomber_jac_right_cuff_left = models.ForeignKey(ImageField, related_name='bomber_jac_right_cuff_left', null=True, blank=True)
#     bomber_jac_mid_cuff_left = models.ForeignKey(ImageField, related_name='bomber_jac_mid_cuff_left', null=True, blank=True)
#     bomber_jac_bottom_cuff_left = models.ForeignKey(ImageField, related_name='bomber_jac_bottom_cuff_left', null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class BomberJacket_Right(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Bomber Jacket Right')
#
#     bomber_jac_mid_body_right = models.ForeignKey(ImageField, related_name='bomber_jac_mid_body_right', null=True, blank=True)
#     bomber_jac_left_body_right = models.ForeignKey(ImageField, related_name='bomber_jac_left_body_right', null=True, blank=True)
#     bomber_jac_right_body_right = models.ForeignKey(ImageField, related_name='bomber_jac_right_body_right', null=True, blank=True)
#     bomber_jac_bottom_body_right = models.ForeignKey(ImageField, related_name='bomber_jac_bottom_body_right', null=True, blank=True)
#     bomber_jac_left_cuff_right = models.ForeignKey(ImageField, related_name='bomber_jac_left_cuff_right', null=True, blank=True)
#     bomber_jac_right_cuff_right = models.ForeignKey(ImageField, related_name='bomber_jac_right_cuff_right', null=True, blank=True)
#     bomber_jac_mid_cuff_right = models.ForeignKey(ImageField, related_name='bomber_jac_mid_cuff_right', null=True, blank=True)
#     bomber_jac_bottom_cuff_right = models.ForeignKey(ImageField, related_name='bomber_jac_bottom_cuff_right', null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class BomberJacket_Back(TimeStampedModel):
#     name = models.CharField(max_length=250, help_text='Bomber Jacket Back')
#
#     bomber_jac_body_back = models.ForeignKey(ImageField, related_name='bomber_jac_body_back', on_delete=models.CASCADE, null=True, blank=True)
#     bomber_jac_collar_back = models.ForeignKey(ImageField, related_name='bomber_jac_collar_back', on_delete=models.CASCADE, null=True, blank=True)
#     bomber_jac_hem_back = models.ForeignKey(ImageField, related_name='bomber_jac_hem_back', on_delete=models.CASCADE, null=True, blank=True)
#     bomber_jac_left_sleeve_back = models.ForeignKey(ImageField, related_name='bomber_jac_left_back', on_delete=models.CASCADE, null=True, blank=True)
#     bomber_jac_right_sleeve_back = models.ForeignKey(ImageField, related_name='bomber_jac_right_back', on_delete=models.CASCADE, null=True, blank=True)
#     bomber_jac_left_cuff_back = models.ForeignKey(ImageField, related_name='bomber_jac_left_cuff_back', on_delete=models.CASCADE, null=True, blank=True)
#     bomber_jac_right_cuff_back = models.ForeignKey(ImageField, related_name='bomber_jac_right_cuff_back', on_delete=models.CASCADE, null=True, blank=True)
#     bomber_jac_left_sleeve_design_back = models.ForeignKey(ImageField, related_name='bomber_jac_left_sleeve_design_back', on_delete=models.CASCADE, null=True, blank=True)
#
#     class Meta:
#         get_latest_by = 'updated_at'
#         ordering = ('-updated_at', '-created_at',)
#
#     def __str__(self):
#         return f"{self.name}"

class Towel(TimeStampedModel):
    name = models.CharField(max_length=250, help_text='Towel Front')
    display_image = models.ImageField(upload_to='uploads/display')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    towel_front = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='towel_front')
    towel_back = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='towel_back')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class LeftView(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Left View")
    left_v_body_view = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_v_body_view',
                                         blank=True, null=True)
    left_v_upper_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_v_upper_part',
                                          blank=True, null=True)
    left_v_lower_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_v_lower_part',
                                          blank=True, null=True)
    left_v_left_s_upper = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_v_left_s_upper', null=True, blank=True)
    left_v_left_s_lower = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_v_left_s_lower', null=True, blank=True)
    left_v_right_s_upper = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_v_right_s_upper', null=True, blank=True)
    left_v_right_s_lower = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='left_v_right_s_lower', null=True, blank=True)


    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class RightView(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Right View")
    right_v_body_view = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='right_v_body_view',
                                          blank=True, null=True)
    right_v_upper_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='right_v_upper_part',
                                           blank=True, null=True)
    right_v_lower_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='right_v_lower_part',
                                           blank=True, null=True)

    right_v_left_s_upper = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='right_v_left_s_upper',
                                            null=True, blank=True)
    right_v_left_s_lower = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='right_v_left_s_lower',
                                            null=True, blank=True)
    right_v_right_s_upper = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='right_v_right_s_upper',
                                             null=True, blank=True)
    right_v_right_s_lower = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='right_v_right_s_lower',
                                             null=True, blank=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class BackView(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Back View")
    back_first_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='back_first_part',
                                        blank=True, null=True)
    back_second_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='back_second_part',
                                         blank=True, null=True)
    back_third_part = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='back_third_part',
                                        blank=True, null=True)
    back_left_sleeve = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='back_left_sleeve',
                                         blank=True, null=True)
    back_right_sleeve = models.ForeignKey(ImageField, on_delete=models.CASCADE, related_name='back_right_sleeve',
                                          blank=True, null=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class DesignImages(TimeStampedModel):
    name = models.CharField(max_length=200, help_text="DesignImages")
    image = models.ImageField(upload_to='uploads/body')

    # image_left = models.ImageField(upload_to='uploads/body')
    # image_right = models.ImageField(upload_to='uploads/body')

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"


class ProductDesign(TimeStampedModel):
    name = models.CharField(max_length=250, help_text="Product Design Name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    display_image = models.ImageField(upload_to='uploads/display')
    front_view = models.ForeignKey(Body, on_delete=models.CASCADE)
    back_view = models.ForeignKey(BackView, on_delete=models.CASCADE)
    left_view = models.ForeignKey(LeftView, on_delete=models.CASCADE, null=True, blank=True)
    right_view = models.ForeignKey(RightView, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)

    def __str__(self):
        return f"{self.name}"
