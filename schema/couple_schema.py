from pydantic import BaseModel, Field
from typing import List, Optional


# ---------------- PERSON ANALYSIS ----------------

class RelationshipPerson(BaseModel):
    love_personality: str
    emotional_depth: str
    attachment_style: str
    strengths_in_love: str
    weaknesses_in_love: str


# ---------------- COMPATIBILITY SCORES ----------------

class RelationshipCompatibilityScores(BaseModel):
    emotional_compatibility: int = Field(ge=0, le=100)
    romantic_attraction: int = Field(ge=0, le=100)
    communication_compatibility: int = Field(ge=0, le=100)
    trust_level: int = Field(ge=0, le=100)
    long_term_stability: int = Field(ge=0, le=100)
    overall_love_compatibility: int = Field(ge=0, le=100)


# ---------------- LOVE DYNAMICS ----------------

class LoveDynamics(BaseModel):
    who_loves_more: str
    who_is_more_expressive: str
    who_is_more_reserved: str
    emotional_leader: str
    balance_description: str


# ---------------- EMOTIONAL CONNECTION ----------------

class EmotionalConnection(BaseModel):
    bond_depth: str
    emotional_safety: str
    attraction_intensity: str
    natural_connection: str


# ---------------- STRENGTHS ----------------

class RelationshipStrengths(BaseModel):
    strengths: List[str]


# ---------------- CHALLENGES ----------------

class RelationshipChallenges(BaseModel):
    challenges: List[str]
    conflict_areas: List[str]


# ---------------- DESTINY ANALYSIS ----------------

class DestinyAnalysis(BaseModel):
    relationship_type: str  # soulmate, karmic, twin flame, etc.
    long_term_potential: str
    marriage_potential: str
    destiny_alignment: str


# ---------------- TIMELINE ----------------

class RelationshipTimeline(BaseModel):
    near_future: str
    middle_phase: str
    long_term_outcome: str


# ---------------- AURA ----------------

class CombinedLoveAura(BaseModel):
    aura_color: str
    energy_description: str
    attraction_field: str


# ---------------- FINAL ARCHETYPE ----------------

class RelationshipArchetype(BaseModel):
    name: str
    description: str


# ---------------- MAIN RESPONSE ----------------

class RelationshipPalmResponse(BaseModel):
    person_1: RelationshipPerson
    person_2: RelationshipPerson

    compatibility_scores: RelationshipCompatibilityScores
    love_dynamics: LoveDynamics
    emotional_connection: EmotionalConnection

    strengths_of_relationship: RelationshipStrengths
    challenges_and_conflicts: RelationshipChallenges

    destiny_analysis: DestinyAnalysis
    relationship_timeline: RelationshipTimeline

    combined_love_aura: CombinedLoveAura
    relationship_archetype: RelationshipArchetype