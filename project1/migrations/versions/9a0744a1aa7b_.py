"""empty message

Revision ID: 9a0744a1aa7b
Revises: 7cbde3c5ea67
Create Date: 2022-04-28 20:37:37.857330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a0744a1aa7b'
down_revision = '7cbde3c5ea67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_question'))
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name=op.f('fk_answer_question_id_question'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_answer'))
    )
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_car_person_no_person'), 'person', ['person_no'], ['no'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_car_person_no_person'), type_='foreignkey')

    op.drop_table('answer')
    op.drop_table('question')
    # ### end Alembic commands ###