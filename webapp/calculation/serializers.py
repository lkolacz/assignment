import json
import logging
from rest_framework import serializers
from .helpers import recur_sum, get_sha256_hexdigest

logger = logging.getLogger(__name__)


class SumEndpointSerializer(serializers.BaseSerializer):

    def to_internal_value(self, data):
        try:
            data = json.loads(data)
            result = recur_sum(data)
            result = get_sha256_hexdigest(result)
        except Exception as expt:
            logger.error(expt)
            raise serializers.ValidationError({
                'payload': 'Payload is incorrect.'
            })
        # Return the validated values. This will be available as the `.validated_data` property.
        return {
            'SHA256_hash_of_the_sum': result,
        }

    def to_representation(self, instance):
        return instance
