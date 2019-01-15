# -*- coding: utf-8 -*-

"""
Object type for topic

"""

from collections import namedtuple
from .wrapper import namedtuple_with_defaults

Topic = namedtuple_with_defaults(
    namedtuple('Topic',
               [
                   'briefIntro',
                   'content',
                   'createdAt',
                   'enableForUserPost',
                   'enablePictureWatermark',
                   'enablePictureComments',
                   'friendsAlsoSubscribe',
                   'id',
                   'isAnonymous',
                   'isDreamTopic',
                   'isUserTopicAdmin',
                   'isCommentForbidden',
                   'isValid',
                   'keywords',
                   'tips',
                   'tabs',
                   'lastMessagePostTime',
                   'likeIcon',
                   'maintainer',
                   'messagePrefix',
                   'newCategory',
                   'operateStatus',
                   'pictureUrl',
                   'rectanglePicture',
                   'entryTab',
                   'preferSection',
                   'inShortcuts',
                   'ref',
                   'squarePicture',
                   'subscribedAt',
                   'subscribedStatusRawValue',
                   'subscribersTextSuffix',
                   'subscribersCount',
                   'subscribersName',
                   'subscribersDescription',
                   'toppingArea',
                   'thumbnailUrl',
                   'timeForRank',
                   'topicId',
                   'topicType',
                   'type',
                   'botCount',
                   'updatedAt'
               ])
)
