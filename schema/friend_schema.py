from pydantic import BaseModel, Field
from typing import List, Optional


class FriendPerson(BaseModel):
    personality: Optional[str] = None
    emotional_nature: Optional[str] = None
    intelligence_style: Optional[str] = None
    social_behavior: Optional[str] = None
    hidden_strength: Optional[str] = None
    main_weakness: Optional[str] = None


class CompatibilityScores(BaseModel):
    emotional_compatibility: Optional[int] = Field(default=None, ge=0, le=100)
    communication_compatibility: Optional[int] = Field(default=None, ge=0, le=100)
    trust_compatibility: Optional[int] = Field(default=None, ge=0, le=100)
    teamwork_compatibility: Optional[int] = Field(default=None, ge=0, le=100)
    overall_compatibility: Optional[int] = Field(default=None, ge=0, le=100)


class PersonalityDynamics(BaseModel):
    who_is_more_emotional: Optional[str] = None
    who_is_more_logical: Optional[str] = None
    who_leads_naturally: Optional[str] = None
    who_is_more_supportive: Optional[str] = None
    balance_between_them: Optional[str] = None


class EmotionalConnection(BaseModel):
    bond_type: Optional[str] = None
    emotional_depth: Optional[int] = Field(default=None, ge=0, le=100)
    trust_level: Optional[int] = Field(default=None, ge=0, le=100)
    communication_flow: Optional[str] = None
    emotional_balance: Optional[str] = None


class StrengthsOfBond(BaseModel):
    strengths: Optional[List[str]] = None


class ChallengesAndGrowth(BaseModel):
    challenges: Optional[List[str]] = None
    growth_opportunities: Optional[List[str]] = None


class DestinyAlignment(BaseModel):
    alignment_type: Optional[str] = None
    future_tendency: Optional[str] = None
    long_term_potential: Optional[str] = None


class FriendshipTimeline(BaseModel):
    near_future: Optional[str] = None
    middle_phase: Optional[str] = None
    long_term_outcome: Optional[str] = None


class CombinedAura(BaseModel):
    aura_color: Optional[str] = None
    energy_description: Optional[str] = None
    bond_energy_type: Optional[str] = None


class ConnectionArchetype(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class FriendPalmResponse(BaseModel):
    person_1: Optional[FriendPerson] = None
    person_2: Optional[FriendPerson] = None

    compatibility_scores: Optional[CompatibilityScores] = None
    personality_dynamics: Optional[PersonalityDynamics] = None
    emotional_connection: Optional[EmotionalConnection] = None

    strengths_of_bond: Optional[StrengthsOfBond] = None
    challenges_and_growth: Optional[ChallengesAndGrowth] = None

    destiny_alignment: Optional[DestinyAlignment] = None
    friendship_timeline: Optional[FriendshipTimeline] = None

    combined_aura: Optional[CombinedAura] = None
    connection_archetype: Optional[ConnectionArchetype] = None